import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Item


class Command(BaseCommand):
    help = 'Items sold in stores'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Item name')
        parser.add_argument('description', type=str, help='Description of item')
        parser.add_argument('price', type=float, help='Price of item')
        parser.add_argument('amount', type=int, help='Amoune of items')
    
    def handle(self, *args, **kwargs):
        item = Item(name=kwargs.get('name'),
                    description=kwargs.get('description'),
                    price=kwargs.get('price'),
                    amount=kwargs.get('amount'),
                    date_add=datetime.datetime.now())
        item.save()
        