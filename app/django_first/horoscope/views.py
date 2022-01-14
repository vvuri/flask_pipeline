from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def zodiac_sign(request, sign):
    if sign == 'leo':
        return HttpResponse("Page leo!")
    elif sign == 'taurus':
        return HttpResponse("Page taurus!")
    else:
        return HttpResponseNotFound("404 !!!")
