import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sem_app_2.models import Author, Article, Commentary, Order, Item, Client
# Create your views here.


def get_authors(request):
    context = dict()
    context['title'] = 'List of authors'
    context['authors'] = Author.objects.all()
    context['text'] = f'There is the list of {len(context["authors"])} authors.'
    # file = open('seminar/sem_app_2/templates/sem_app_2/authors.html', 'r')
    return render(request, 'sem_app_2/authors.html', context=context)

def get_articles(request, author_id):
    context = dict()
    articles = Article.objects.all().filter(author_id=author_id)
    author = Author.objects.get(pk=author_id)
    context['title'] = f'{author.full_name} articles'
    context['text'] = f'List of articles of author {author.name}'
    context['articles'] = articles
    return render(request, 'sem_app_2/articles.html', context=context)

def get_article(request, article_id):
    context = dict()
    article = Article.objects.filter(id=article_id).first()
    article.views += 1
    article.save()
    context['title'] = 'Commentaries of article'
    context['text'] = f'Text of the article {article_id}'
    context['article'] = article
    context['commentaries'] = Commentary.objects.all().filter(article_id=article_id)
    return render(request, 'sem_app_2/article.html', context=context)

def get_orders(request):
    context = dict()
    context['text'] = 'All orders:'
    context['orders'] = Order.objects.all()
    return render(request, 'sem_app_2/orders.html', context=context)

def get_client_items(request, client_id):
    context = dict()
    context['title'] = 'Client orders'
    context['client'] = Client.objects.get(id=client_id)
    context['text'] = 'Every order of the client'
    orders = Order.objects.all().filter(client_id=client_id)
    
    context['orders'] = orders
    items_0 = list()
    items_7 = list()
    items_30 = list()
    items_365 = list()
    
    today = datetime.datetime.today()
    tz_info = today.tzinfo
    for order in orders.all():
        # for item in order.items.all():
        tz_info_order = order.date_order.tzinfo
        
        today = today.replace(tzinfo=tz_info_order)

        delta = today - order.date_order
        if delta < datetime.timedelta(days=7):
            items = order.items.all()
            for item in items:
                items_0.append(item)
                items_7.append(item)
        elif delta < datetime.timedelta(days=30):
            items = order.items.all()
            for item in items:
                items_0.append(item)
                items_30.append(item)
        elif delta < datetime.timedelta(days=365):
            items = order.items.all()
            for item in items:
                items_0.append(item)
                items_365.append(item)
    context['items_0'] = items_0
    context['items_7'] = items_7
    context['items_30'] = items_30
    context['items_365'] = items_365
    return render(request, 'sem_app_2/client.html', context=context)


def get_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'sem_app_2/items.html', context=context)
