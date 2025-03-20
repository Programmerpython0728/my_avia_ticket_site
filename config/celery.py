import os
from celery import Celery
os.environ.setdefault("DJANGO_SITTINGS_MODULE",'config.settings')

app=Celery('my_avia_kassa')

app.config_from_object('django.conf:sittings',namespace='Celery')
app.autodiscover_tasks()
