import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Author


class Command(BaseCommand):
    help = 'Creating author'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of author')
        parser.add_argument('last_name', type=str, help='Lastname of author')
        parser.add_argument('full_name', type=str, help='Full name of author')
        parser.add_argument('email', type=str, help='E-mail of author')
        parser.add_argument('biography', type=str, help='Biography of author')

    def handle(self, *args, **kwargs):
        # name:str = kwargs.get('name'),
        # last_name:str = kwargs.get('last_name'),
        # full_name:str = kwargs.get('full_name'),
        # email:str = kwargs.get('email'),
        # biography:str = kwargs.get('biography'),
        # birhtday:datetime = datetime.datetime.now()
        author = Author(name=kwargs.get('name'),
                        last_name=kwargs.get('last_name'),
                        full_name=kwargs.get('full_name'),
                        email=kwargs.get('email'),
                        biography=kwargs.get('biography'),
                        birthday=datetime.datetime.now())
        author.save()
        self.stdout.write(f'{author}')
