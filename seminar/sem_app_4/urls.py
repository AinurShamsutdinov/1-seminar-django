from django.urls import path, include
from . import views

urlpatterns = [
    path('choice/', views.get_choice_page, name='get_choice_page'),
    path('author/', views.add_author, name='add_author'),
    path('article/', views.add_article, name='add_article'),
]
