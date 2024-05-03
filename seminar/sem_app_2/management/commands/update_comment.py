import datetime

from django.core.management.base import BaseCommand
from sem_app_2.models import Commentary


class Command(BaseCommand):
    help = 'Update commentary for comment by ID'

    def add_arguments(self, parse):
        parse.add_argument('id', type=int, help='Comment ID')
        parse.add_argument('comment', type=str, help='Commentary')

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        new_comment = kwargs.get('comment')
        commentary = Commentary.objects.filter(id=id).first()
        commentary.comment = new_comment
        commentary.date_edit = datetime.datetime.now()
        commentary.save()
        self.stdout.write('Updated commentary with ID={id}')
