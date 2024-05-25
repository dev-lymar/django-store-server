import os

import django
import environ
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()

env = environ.Env(
    SUPERUSER_USERNAME=(str),
    SUPERUSER_EMAIL=(str),
    SUPERUSER_PASSWORD=(str),
)

User = get_user_model()
username = env("SUPERUSER_USERNAME")
email = env("SUPERUSER_EMAIL")
password = env("SUPERUSER_PASSWORD")

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Superuser {username} already exists")
