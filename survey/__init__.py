import os

from configurations import importer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

importer.install(check_options=True)
