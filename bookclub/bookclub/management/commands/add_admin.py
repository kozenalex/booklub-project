import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Adds a django admin user'

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USER', 'admin')
        password = os.getenv('ADMIN_PASSWORD', 'Qwerty123')
        user = User.objects.filter(username=username).first()
        if not user:
            User.objects.create_superuser(username=username, password=password, email='')

        self.stdout.write(self.style.SUCCESS('Successfully added admin user'))