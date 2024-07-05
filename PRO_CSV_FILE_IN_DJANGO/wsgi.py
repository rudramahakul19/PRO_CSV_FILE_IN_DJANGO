"""
WSGI config for PRO_CSV_FILE_IN_DJANGO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRO_CSV_FILE_IN_DJANGO.settings')

application = get_wsgi_application()
