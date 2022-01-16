from django.urls import path
from horoscope import views


urlpatterns = [
    path('', views.index),
    path('<int:sign>', views.zodiac_sign_by_number),
    path('<str:sign>', views.zodiac_sign, name='horoscope-name')
]