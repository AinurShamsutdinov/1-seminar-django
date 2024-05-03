from django.core.management.base import BaseCommand
from sem_app_2.models import Author, Article


class Command(BaseCommand):
    help = 'Get articles by the name of the author'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('amount', type=int, help='Amount of articles')

    def handle(self, *args, **kwargs):
        author_name = kwargs.get('name')
        amount = kwargs.get('amount')
        authors = Author.objects.all().filter(name=author_name)
        articles = list()
        for author in authors:
            author_arts = Article.objects.all().filter(author_id=author.id)[:amount]
            if len(author_arts) > 0: 
                articles.append(author_arts)
            for art in author_arts:
                self.stdout.write(f'Article ID{art.id} {art.content}')
        self.stdout.write(f'Amount of articles: {articles}')
