from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {
    'leo': 'Page leo!',
    'taurus': 'Page taurus!'
}


def index(request):
    return HttpResponse('List of zodiacs')


def zodiac_sign(request, sign: str):
    text_page = zodiac_dict.get(sign, None)
    data = {'inner': text_page, }
    render_page = render_to_string('horoscope/info.html', context=data)
    if text_page:
        return HttpResponse(render_page)
    else:
        return HttpResponseNotFound(f"Zodiac page - 404 for {sign}")


def zodiac_sign_by_number(request, sign: int):
    text_page = list(zodiac_dict)
    if sign > len(text_page) or sign == 0:
        return HttpResponse(f"Route with int type: {sign}")
    name_zodiac = text_page[sign-1]
    redirect_urls = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponse(redirect_urls)  # HttpResponse(name_zodiac)

