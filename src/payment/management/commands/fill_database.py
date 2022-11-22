from django.core.management.base import BaseCommand

from payment.models import Item


class Command(BaseCommand):
    help = "Creates a superuser if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--count', help="How many random items insert into database")

    def handle(self, *args, **kwargs):
        for i in range(int(kwargs['count'])):
            item = Item(name='test_name_' + str(i + 1),
                        description='test_title_' + str(i + 1),
                        price=float(2 * i + 2))
            item.save()
