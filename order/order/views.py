import time

from django import http
from django.shortcuts import render, HttpResponse
from django.conf import settings
import logging

logger = logging.getLogger('goods.views')
tracing = settings.OPENTRACING_TRACING

@tracing.trace()
def order_index(request):
    child_span = tracing.tracer.start_active_span("order_index")
    order_info = order(1, 3)
    print("order_index")
    child_span.close()
    return HttpResponse("{} {} order_info: {}".format("order", "index", order_info))

def order(a, b):
    child_span = tracing.tracer.start_active_span("func_order")
    print("order views order")
    child_span.close()
    return "{}".format(a+b)


