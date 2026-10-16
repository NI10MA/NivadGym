import os

from django.core.wsgi import get_wsgi_application

# Django settings module for WSGI servers.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nivad_gym.settings")

application = get_wsgi_application()
