import logging
import random
import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import RandomForm, AuthorForm, ArticleForm, CommentForm, ItemForm
from sem_app_2.models import Author as AuthorModel
from sem_app_2.models import Article as ArticleModel
from sem_app_2.models import Commentary as CommentModel
from sem_app_2.models import Item as ItemModel


logger = logging.getLogger(__name__)

# Create your views here.


# from 1-3 seminars
def head_tails(request, toss):
    results = list()
    for i in range(toss):
        rand = random.randrange(0, 2)
        result: str
        if rand == 0:
            result = 'Heads'
        else:
            result = 'Tails'
        results.append(result)
    logger.info(f'Head or tails page accessed {results}')
    return render(request, 'randomapp/coin.html', {'results': results, 'toss': toss})


def dice(request, toss):
    results = list()
    for i in range(toss):
        rand = random.randrange(1, 7)
        results.append(rand)
    logger.info(f'Dice page accessed {results}')
    return render(request, 'randomapp/dice.html', {'results': results, 'toss': toss})


def random_generate(request, generations):
    results = list()
    for i in range(generations):
        rand = random.randrange(0, 101)
        results.append(rand)
    logger.info(f'Random from 0 to 100 is {results}')
    return render(request, 'randomapp/random.html', {'results': results, 'generations': generations})


def main(request):
    links = list()
    links.append('headtail')
    links.append('dice')
    links.append('random')
    context = {
        'links': links,
        'title': 'Main page title',
        'page': 'This is main page with links: ',
    }
    return render(request, 'randomapp/main.html', context)


def about(request):
    context = {
        'title': 'About page title',
        'page': 'This is page created by me, who learns django framework.',
    }
    return render(request, 'randomapp/about.html', context)

# 4 seminar

def get_choice_page(request):
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            random = form.cleaned_data['random']
            amount = form.cleaned_data['amount']
            print(f'Choice recie ved: {random=} {amount=}')
            if random == 'dice':
                return redirect(f'/random/dice/{amount}')
            elif random == 'coin':
                return redirect(f'/random/coin/{amount}')
            elif random == 'random':
                return redirect(f'/random/random/{amount}')
    else:
        form = RandomForm()
    return render(request, 'sem_app_4/choice.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            full_name = f'{name} {last_name}'
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author  = AuthorModel(name=name, last_name=last_name, full_name=full_name, email=email, biography=biography, birthday=birthday)
            author.save()
    else:
        form = AuthorForm()
    return render(request, 'sem_app_4/author.html', {'form': form})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            head = form.cleaned_data['head']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = AuthorModel.objects.get(pk=int(form.cleaned_data['authors']))
            category = form.cleaned_data['category']
            published = form.cleaned_data['published']
            article = ArticleModel(head=head, 
                                   content=content,
                                   publish_date=publish_date,
                                   author=author,
                                   category=category,
                                   published=published
                                   )
            article.save()
    else:
        form = ArticleForm()
    return render(request, 'sem_app_4/add_article.html', {'form': form})


def get_article(request, article_id):
    context = {}
    context['text'] = 'Article and commentaries'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            article = ArticleModel.objects.get(pk=article_id)
            author = AuthorModel.objects.get(pk=article.pk)
            comment = form.cleaned_data['comment']
            date_creat = datetime.datetime.now()
            commentary = CommentModel(author=author, article=article, comment=comment, date_creat=date_creat)
            commentary.save()
    context['article'] = ArticleModel.objects.get(pk=article_id)
    context['commentaries'] = CommentModel.objects.all().filter(article_id=article_id)
    context['form'] = CommentForm()
    return render(request, 'sem_app_4/article.html', context=context)


def edit_item(request, item_id):
    context = {}
    context['text'] = 'Edit item'
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            date_add = form.cleaned_data['date_add']
            image = form.cleaned_data['image']
            item = ItemModel.objects.get(pk=item_id)
            item.name = name
            item.description = description
            item.price = price
            item.amount = amount
            item.date_add = date_add
            item.image = image
            item.save()
    item = ItemModel.objects.get(pk=item_id)
    form = ItemForm(initial={
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'amount': item.amount,
            'date_add': item.date_add,
            'image': item.image
        })
    context['form'] = form
    return render(request, 'sem_app_4/edit_item.html', context=context)


def index(request):
    apps = list()
    apps.append(['random/main', 'Semianar 1. Random generator main page.'])
    apps.append(['sem_1', 'Seminar 1. Index page.'])
    apps.append(['sem_1/aboutme', 'Seminar 1. About me page'])
    apps.append(['sem_2/authors', 'Seminar 2. Authors page'])
    apps.append(['sem_2/orders', 'Seminar 2. Orders page'])
    apps.append(['sem_2/items', 'Seminar 2. Items page'])
    apps.append(['sem_4/choice', 'Seminar 4. Page with choice of random generator'])
    apps.append(['sem_4/author', 'Seminar 4. Add author page'])
    apps.append(['sem_4/add/article', 'Seminar 4. Add article page'])
    context = {
        'apps': apps,
    }

    return render(request, 'sem_app_4/index.html', context=context)
