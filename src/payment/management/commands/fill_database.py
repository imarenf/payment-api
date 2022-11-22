from django.core.management.base import BaseCommand

from payment.models import Item


class Command(BaseCommand):
    help = "Fills database with test values if it is empty"

    def add_arguments(self, parser):
        parser.add_argument('--count', help="How many random items insert into database")

    def handle(self, *args, **kwargs):
        items = Item.objects.all()
        if len(items) > 0:
            return
        for i in range(int(kwargs['count'])):
            item = Item(name='test_name_' + str(i + 1),
                        description='test_title_' + str(i + 1),
                        price=float(2 * i + 2))
            item.save()
