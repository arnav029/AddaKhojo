from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create or reset the admin superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'admin'
        password = 'admin123'
        email = 'admin@aawaaragardi.local'

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" password reset.'))
