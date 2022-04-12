import json
import os
import time

from django import http
import requests
from django.shortcuts import render, HttpResponse
from django.conf import settings
import logging
from opentracing.propagation import Format
import django_opentracing
import opentracing
import requests

logger = logging.getLogger('microservice.views')
tracing = settings.OPENTRACING_TRACING


@tracing.trace()
#@tracing.trace(view=False)
def total(request):
    hostname = request.get_host().split(":")[0]
    return HttpResponse("{} {} order_info: {}".format("total", call_goods(hostname), call_order(hostname)))


#@tracing.trace()
#@tracing.trace(view=False)
def call_order(Hostname):
    order_url = "http://{}:8080/order/".format(Hostname)
    print("call_order")
    time.sleep(3)
    tracer = opentracing.global_tracer()
    span = tracer.active_span
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)
    res = requests.get(order_url, headers=headers, timeout=3.0)
    return res.text


#@tracing.trace()
#@tracing.trace(view=False)
def call_goods(Hostname):
    order_url = "http://{}:8000/goods/".format(Hostname)
    headers = {}
    print("call_goods")
    time.sleep(2)
    tracer = opentracing.global_tracer()
    span = tracer.active_span
    tracer.inject(span, Format.HTTP_HEADERS, headers)
    res = requests.get(order_url, headers=headers, timeout=3.0)
    return res.text

