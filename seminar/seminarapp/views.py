import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world!')


def aboutme(request):
    return HttpResponse('This page is about me.')
