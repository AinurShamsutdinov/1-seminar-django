from datetime import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str, help='Name of client')
        parser.add_argument('item_names', type=str, help='Names of item')
        parser.add_argument('date', type=str, help='Time of order')
        
    def handle(self, *args, **kwargs):
        client = Client.objects.get(name=kwargs.get('client_name'))
        order = Order.objects.all().filter(client_id=client.id).first()
        name_items = kwargs.get('item_names').split(' ')
        date_order = datetime.strptime(kwargs.get('date'), '%b %d %Y %I:%M%p').date()
        item = Item.objects.all().filter(name=kwargs.get('item_name')).first()
        order = Order(client=client, full_price=0, date_order=date_order)
        order.save()
        for name_item in name_items:
            item = Item.objects.all().filter(name=name_item).first()
            if order.items.count() == 0:
                order.items.set([item])              
            else:
                order.items.add(item)
            order.full_price += item.price
            order.save()
