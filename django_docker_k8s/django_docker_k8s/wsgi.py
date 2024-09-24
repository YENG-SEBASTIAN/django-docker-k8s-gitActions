"""
WSGI config for django_docker_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
import pathlib
from django.core.wsgi import get_wsgi_application
import dotenv

# Set the path to the .env file
dotenv_path = pathlib.Path(__file__).resolve().parent.parent / '.env'

# Load environment variables from the .env file if it exists
if dotenv_path.is_file():
    dotenv.load_dotenv(dotenv_path)

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_docker_k8s.settings')

# Get the WSGI application
application = get_wsgi_application()
