import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'core' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create the WSGI application object.
app = get_wsgi_application()
