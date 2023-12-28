from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='dronov9@yandex.ru',
            first_name='dronov9',
            last_name='OnlineStore',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('qwerty')
        user.save()
