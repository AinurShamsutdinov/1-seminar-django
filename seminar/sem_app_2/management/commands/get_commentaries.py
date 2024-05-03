from django.core.management.base import BaseCommand
from sem_app_2.models import Commentary, Article, Author


class Command(BaseCommand):
    help = 'Get author commentaries'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('amount', type=int, help='Amount of commentaries')

    def handle(self, *args, **kwargs):
        author_name = kwargs.get('name')
        amount = kwargs.get('amount')
        author = Author.objects.filter(name=author_name).first()
        author_comments = Commentary.objects.all().filter(author_id = author.id)[:amount]
        for comment in author_comments:
            self.stdout.write(f'Comment: {comment.comment}, Author: {author.name}')
