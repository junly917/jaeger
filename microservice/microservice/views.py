import json
import os
import time
from cv2 import trace

from django import http
import requests
from django.shortcuts import render, HttpResponse
from django.conf import settings
import logging
from opentracing.propagation import Format
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import django_opentracing
import opentracing
import requests

logger = logging.getLogger('microservice.views')
tracing = settings.OPENTRACING_TRACING


@tracing.trace()
def total(request):
    hostname = request.get_host().split(":")[0]
    #return HttpResponse("total order_info: {}".format(hostname)) 
    return HttpResponse("{} {} order_info: {}".format("total", call_goods(hostname), call_order(hostname)))


def call_order(Hostname):
  child_span = tracing.tracer.start_active_span("child call_order")
  order_url = "http://{}:{}/order/".format(os.getenv('ORDER_SERVICE_HOST'), os.getenv('ORDER_SERVICE_PORT'))
  # order_url = "http://{}:{}/order/".format('127.0.0.1', 8002)

  print("call_order")
  tracer = opentracing.global_tracer()     # 用于将span和trace进行透传
  span = tracer.active_span
  headers = {}
  tracer.inject(span, Format.HTTP_HEADERS, headers)
  res = requests.get(order_url, headers=headers, timeout=3.0)
  child_span.close()
  return res.text


def call_goods(Hostname):
  child_span = tracing.tracer.start_active_span("child call_goods")
  # goods_url = "http://{}:{}/goods/".format('127.0.0.1', 8001)
  goods_url = "http://{}:{}/goods/".format(os.getenv('GOODS_SERVICE_HOST'), os.getenv('GOODS_SERVICE_PORT'))
  headers = {}
  print("call_goods")
  time.sleep(2)
  tracer = opentracing.global_tracer() 
  span = tracer.active_span
  tracer.inject(span, Format.HTTP_HEADERS, headers)   # 用于将span和trace进行透传
  res = requests.get(goods_url, headers=headers, timeout=3.0)
  child_span.close()
  return res.text


# @tracing.trace()
def trace_id(request):
  child_span = tracing.tracer.start_active_span("child trace_id")
  # order_url = "http://{}:{}/order/".format(os.getenv('ORDER_SERVICE_HOST'), os.getenv('ORDER_SERVICE_PORT'))
  tracer = opentracing.global_tracer()
  span = tracer.active_span
  headers = {}
  tracer.inject(span, Format.HTTP_HEADERS, headers)
  child_span.close()
  return HttpResponse("res.text")