import time

from django import http
from django.shortcuts import render, HttpResponse


def order_index(request):
    order_info = order(1, 3)
    print("order_index")
    return HttpResponse("{} {} order_info: {}".format("order", "index", order_info))


def order(a, b):
    print("order views order")
    return "{}".format(a+b)


