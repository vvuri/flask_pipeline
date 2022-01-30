from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import News


def index(request):
    news = News.objects.order_by('-create_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


def movie(request):
    render_page = render_to_string('news/movie_list.html')  # , context=data)
    return HttpResponse(render_page)
