import datetime

from django.core.management.base import BaseCommand, CommandParser
from sem_app_2.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(id=kwargs.get('id')).first()
        items = order.items.count()
        for item in order.items.all():
            self.stdout.write(f'Item: {item}')
        self.stdout.write(f'Amount of items: {items}')
