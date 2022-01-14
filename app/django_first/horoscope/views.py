from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

zodiac_dict = {
    'leo': 'Page leo!',
    'taurus': 'Page taurus!'
}


def zodiac_sign(request, sign: str):
    text_page = zodiac_dict.get(sign, None)
    if text_page:
        return HttpResponse(text_page)
    else:
        return HttpResponseNotFound(f"Zodiac page - 404 for {sign}")


def zodiac_sign_by_number(request, sign: int):
    return HttpResponse(f"Route with int type: {sign}")
