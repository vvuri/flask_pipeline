from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    render_page = render_to_string('news/movie_list.html')  #, context=data)
    return HttpResponse(render_page)
