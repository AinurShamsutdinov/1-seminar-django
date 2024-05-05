import logging
import random
import datetime

from django.shortcuts import render, redirect
from .forms import RandomForm, AuthorForm, ArticleForm, CommentForm
from sem_app_2.models import Author as AuthorModel
from sem_app_2.models import Article as ArticleModel
from sem_app_2.models import Commentary as CommentModel


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
