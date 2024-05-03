from django.urls import path, include
from . import views

urlpatterns = [
    path('authors/', views.get_authors, name='get_authors'),
    path('articles/<int:author_id>/', views.get_articles, name='articles'),
    path('article/<int:article_id>/', views.get_article, name='article'),
    path('orders/', views.get_orders, name='orders'),
    path('client/<int:client_id>/', views.get_client_items, name='get_order_items')
]
