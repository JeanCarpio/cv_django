from django.apps import AppConfig
import os

class CvConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cv"

    def ready(self):
        from django.contrib.auth import get_user_model

        if os.environ.get("RENDER") == "true":
            User = get_user_model()

            username = os.getenv("DJANGO_SUPERUSER_USERNAME")
            email = os.getenv("DJANGO_SUPERUSER_EMAIL")
            password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

            if username and password and not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
