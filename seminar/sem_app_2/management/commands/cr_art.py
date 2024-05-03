import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Article, Author


class Command(BaseCommand):
    help = 'Create article'

    def add_arguments(self, parse):
        parse.add_argument('head', type=str, help='Head of an article')
        parse.add_argument('content', type=str, help='Content of an article')
        parse.add_argument('category', type=str, help='Category of the article')
        parse.add_argument('pk', type=int, help='Author id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # author = Author.objects.filter(id=pk).first()
        author  = Author.objects.get(pk=pk)
        # self.stdout.write(f'{author}')
        head = kwargs.get('head')
        content = kwargs.get('content')
        publish_date = datetime.datetime.now()
        category = kwargs.get('category')
        views = 0
        published = False
        article = Article(head=head, 
                          content=content,
                          publish_date=publish_date, 
                          author=author, 
                          category=category, 
                          views=views, 
                          published=published)
        article.save()
        self.stdout.write(f'{article}')
