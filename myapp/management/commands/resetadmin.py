from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        user, created = User.objects.get_or_create(
            username="LUCIFER"
        )

        user.is_staff = True
        user.is_superuser = True
        user.set_password("BIGBANGTHEORY")
        user.save()

        print("Admin reset successful")