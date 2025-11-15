"""
WSGI entry point for Render when Gunicorn is invoked from the repo root as
`gunicorn job1.wsgi:application`.

This file maps the repository layout (outer `job1/` contains an inner
`job1/` Django project) to a proper DJANGO_SETTINGS_MODULE value so the
application can be loaded without changing Render service settings.
"""
import os

# When Render (or another host) runs `gunicorn job1.wsgi:application` from
# the repository root, the dotted path to the settings module should be
# "job1.job1.settings" (outer job1 -> inner job1 -> settings.py).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "job1.job1.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
