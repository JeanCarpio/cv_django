from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea superusuario automáticamente si no existe'

    def handle(self, *args, **options):
        username = os.environ.get("JeanCarpio")
        email = os.environ.get("berthasuarez459@gmail.com")
        password = os.environ.get("Emelec2026")

        if not username or not password:
            self.stdout.write("Variables de entorno no definidas")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("Superusuario ya existe")
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write("Superusuario creado")
