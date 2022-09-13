import time
from datetime import datetime, timedelta, timezone

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.db import connection


from project.models import *
from django.db.models import Q

from datetime import datetime, timedelta
from django.db import transaction

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler = BackgroundScheduler(timezone='UTC')


@register_job(scheduler, "interval", minutes=10000)
def createprojectvms():
    # from . import bosoperations as ent
    print("createprojectvms  job started! " + str(datetime.now()))
    try:
        pass


    except Exception as e:
        print(e)
        # EntegrasyonErros.objects.create(msg=e, methodname='createprojectvms')
    finally:
        print("createprojectvms  job finished! " + str(datetime.now()))


def start():
    try:
        scheduler.add_jobstore(DjangoJobStore(),'default')
        register_events(scheduler)
        scheduler.start()
        print("Scheduler started!")
    except Exception as e:
        print(e)
