import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'experience_booking.settings')
app = Celery('experience_booking')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
