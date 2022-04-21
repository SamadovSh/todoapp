from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem


class Command(BaseCommand):
    help = u'Displays all tasks completed in the last days (default=3)'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int, default=3)

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        for t in TodoItem.objects.filter(is_completed=True):
            if (now - t.updated).days >= options['days']:
                print('Выполненая задача', t, t.updated)
