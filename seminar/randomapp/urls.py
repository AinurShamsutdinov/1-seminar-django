from django.urls import path, include
from . import views

urlpatterns = [
    path('coin/<int:toss>/', views.head_tails, name='head_tails'),
    path('dice/<int:toss>/', views.dice, name='dice'),
    path('random/<int:generations>/', views.random_generate, name='random_generate'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
]
