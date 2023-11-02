"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

Interface simples e universal para troca de informações entre servidores web
e aplicações criadas com Python.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

application = get_wsgi_application()
