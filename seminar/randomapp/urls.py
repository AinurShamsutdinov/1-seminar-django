from django.urls import path, include
from . import views

urlpatterns = [
    path('headtail/', views.head_tails, name='head_tails'),
    path('dice/', views.dice, name='dice'),
    path('random/', views.random_generate, name='random_generate'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
]
