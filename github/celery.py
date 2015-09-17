__author__ = 'prism'
import os
from celery import Celery
from django.conf import settings
from celery.task.schedules import crontab
from celery.decorators import periodic_task


# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hiren.settings')
app = Celery('hiren')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
