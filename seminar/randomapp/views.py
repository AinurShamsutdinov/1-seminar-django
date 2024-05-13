import logging
import random

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.


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
    links.append('coin')
    links.append('dice')
    links.append('random')
    context = {
        'links': links,
        'title': 'Main page title generate 10 random by default',
        'page': 'This is main page with links: ',
        'about': 'About page',
    }
    return render(request, 'randomapp/main.html', context)


def about(request):
    context = {
        'title': 'About page title',
        'page': 'This is page created by me, who learns django framework.',
    }
    return render(request, 'randomapp/about.html', context)
