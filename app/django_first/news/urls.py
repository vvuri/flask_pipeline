from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from news import views

urlpatterns = [
    path('', views.index),
    # path('<int:sign>', views.movie_sign, name='movie-name')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)