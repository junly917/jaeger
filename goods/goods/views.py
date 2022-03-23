from django import http
from django.shortcuts import render, HttpResponse

from django.conf import settings
import logging

logger = logging.getLogger('goods.views')
tracing = settings.OPENTRACING_TRACING


# @tracing.trace(view=False)
def goods_index(request):
    print("goods_index")
    return HttpResponse("{} {}".format("goods", "index"))

