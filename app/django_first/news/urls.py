from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='news-list'),
    # path('<int:sign>', views.movie_sign, name='movie-name')
    path('movies', views.movie)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
