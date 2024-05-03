import datetime

from django.core.management.base import BaseCommand, CommandParser
from sem_app_2.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        order = Order.objects.all().delete()
        self.stdout.write(f'{order}')
        order = Order.objects.all()
        self.stdout.write(f'{order.count()}')