from django.core.management.base import BaseCommand
from sem_app_2.models import TossCoin


class Command(BaseCommand):
    help = 'Average coin tosses <amount>'

    # add_arguments позволяет парсить командную строку
    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Average coin tosses')

    def handle(self, *args, **kwargs):
        amount = kwargs['amount']
        tosses = TossCoin.objects.all().order_by('-id')[:amount]
        stat = {'Head': 0, 'Tail': 0}
        for toss in tosses:
            if toss.result == 'Head':
                stat[toss.result] += 1
            if toss.result == 'Tail':
                stat[toss.result] += 1
        self.stdout.write(f'{stat}')
