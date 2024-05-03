import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Article, Author


class Command(BaseCommand):
    help = 'Publish article with ID'

    def add_arguments(self, parse):
        parse.add_argument('id', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        article = Article.objects.filter(id=id).first()
        article.published = True
        article.save()
        self.stdout.write(f'{article}')
