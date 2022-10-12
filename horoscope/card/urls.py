from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aries', views.aries, name='aries'),
    path('leo', views.leo, name='leo'),
    path('sagittarius', views.sagittarius, name='sagittarius'),
    path('taurus', views.taurus, name='taurus'),
    path('virgo', views.virgo, name='virgo'),
    path('capricorn', views.capricorn, name='capricorn'),
    path('gemini', views.gemini, name='gemini'),
    path('libra', views.libra, name='libra'),
    path('aquarius', views.aquarius, name='aquarius'),
    path('cancer', views.cancer, name='cancer'),
    path('scorpio', views.scorpio, name='scorpio'),
    path('pisces', views.pisces, name='pisces'),
]