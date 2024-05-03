import datetime
from typing import Any

from django.core.management.base import BaseCommand
from sem_app_2.models import Commentary, Article, Author


class Command(BaseCommand):
    help = 'Create commentary'

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=int, help='Author ID')
        parser.add_argument('article_id', type=int, help='Article ID')
        parser.add_argument('comment', type=str, help='Commentary')

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        article_id = kwargs.get('article_id')
        author = Author.objects.get(pk=author_id)
        article = Article.objects.get(pk=article_id)
        date_creat = datetime.datetime.now()
        commentary = Commentary(author=author,
                             article=article,
                             comment=kwargs.get('comment'),
                             date_creat=date_creat,
                             date_edit=None)
        commentary.save()
