import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application for the project
application = get_wsgi_application()
