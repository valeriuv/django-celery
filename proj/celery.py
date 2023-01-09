import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'UTC'
 
app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "users.tasks.thirty_second_func",
        "schedule": timedelta(seconds=30),
    },
}
 
app.autodiscover_tasks()
 
 