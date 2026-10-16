import os

from django.core.asgi import get_asgi_application

# Django settings module for ASGI servers.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nivad_gym.settings")

application = get_asgi_application()
