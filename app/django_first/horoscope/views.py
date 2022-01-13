from django.shortcuts import render
from django.http import HttpResponse


def leo(request):
    return HttpResponse("Page leo!")


def taurus(request):
    return HttpResponse("Page taurus!")
