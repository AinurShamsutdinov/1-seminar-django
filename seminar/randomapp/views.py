import logging
import random

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.


def head_tails(request):
    rand = random.randrange(0, 2)
    result: str
    if rand == 0:
        result = 'Heads'
    else:
        result = 'Tails'
    logger.info(f'Head or tails page accessed {result}')
    return HttpResponse(f'Head or tails: {result}.')


def dice(request):
    rand = random.randrange(1, 7)
    logger.info(f'Dice page accessed {rand}')
    return HttpResponse(f'Dice is {rand}.')


def random_generate(request):
    rand = random.randrange(0, 101)
    logger.info(f'Random from 0 to 100 is {rand}')
    return HttpResponse(f'Random from 0 to 100 is equal to {rand}.')


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
