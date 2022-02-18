from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = { 'title': 'Список новостей'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_publish=True)


# def index(request):
#     news = News.objects.order_by('-create_at')
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, template_name='news/index.html', context=context)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_publish=True, category_id=self.kwargs['category_id'])


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.filter(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context=context)


def movie(request):
    render_page = render_to_string('news/movie_list.html')  # , context=data)
    return HttpResponse(render_page)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


@csrf_protect
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
