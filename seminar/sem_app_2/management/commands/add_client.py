import datetime
from django.core.management.base import BaseCommand
from sem_app_2.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone', type=str, help='Client phone')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        client = Client(name=kwargs.get('name'),
                        email=kwargs.get('email'),
                        phone=kwargs.get('phone'),
                        address=kwargs.get('address'),
                        date_reg=datetime.datetime.now())
        client.save()