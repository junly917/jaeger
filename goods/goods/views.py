from time import sleep
from django import http
from django.shortcuts import render, HttpResponse

from django.conf import settings
import logging

logger = logging.getLogger('goods.views')
tracing = settings.OPENTRACING_TRACING


@tracing.trace()
def goods_index(request):
    child_span = tracing.tracer.start_active_span("goods_index")
    sleep(0.5)
    print("project： goods")
    res = processes_goods(2, 3)
    child_span.close()
    return HttpResponse("{} {}".format("goods", res))

def processes_goods(a, b):
    child_span = tracing.tracer.start_active_span("func processes_goods")
    sum = int(a) + int(b)
    child_span.close()
    return sum
