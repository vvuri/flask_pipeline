from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import News, Category


def index(request):
    news = News.objects.order_by('-create_at')
    categories = Category.objects.order_by('title')
    context = {
        'news': news,
        'categories': categories,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


def movie(request):
    render_page = render_to_string('news/movie_list.html')  # , context=data)
    return HttpResponse(render_page)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.filter(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)
