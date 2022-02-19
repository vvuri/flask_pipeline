from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from news import views

urlpatterns = [
    # path('', views.index, name='news-list'),
    path('', views.HomeNews.as_view(), name='news-list'),

    # path('<int:sign>', views.movie_sign, name='movie-name')

    # path('category/<int:category_id>/', views.get_category, name='news-category'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='news-category'),

    path('movies', views.movie),

    # path('<int:news_id>/', views.view_news, name='view_news'),
    path('<int:pk>/', views.ViewNews.as_view(), name='view_news'),

    # path('add-news/', views.add_news, name='add-news')
    path('add-news/', views.CreateNews.as_view(), name='add-news'),

    path('__debug__/', include('debug_toolbar.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
