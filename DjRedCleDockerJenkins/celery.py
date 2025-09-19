from celery import Celery
import os 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjRedCleDockerJenkins.settings")


app=Celery("DjRedCleDockerJenkins")
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

# 
from datetime import timedelta
from celery.schedules import crontab


app.conf.beat_schedule={
    "call-every-50-seconds":{
        "task":"api.tasks.visit_cache",
        # "schedule":crontab(minute='*/1') 
        "schedule":timedelta(seconds=50)
    }
}