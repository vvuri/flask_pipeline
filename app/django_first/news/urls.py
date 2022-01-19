from django.urls import path
from news import views

urlpatterns = [
    path('', views.index),
    # path('<int:sign>', views.movie_sign, name='movie-name')
]
