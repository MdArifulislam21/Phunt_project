"""
WSGI config for Phunt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import djangowhitenoise
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Phunt.settings')

application = get_wsgi_application()
application = djangowhitenoise(application)
