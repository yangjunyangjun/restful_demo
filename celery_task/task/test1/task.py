import pytz
from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django_redis import get_redis_connection
# celery -A gaea beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A gaea  worker -l info  --pool=solo
from api.desk import Fa


def device_task():
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='0',
        hour='08',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
        timezone=pytz.timezone('Asia/Shanghai')
    )
    try:
        PeriodicTask.objects.get(name='add device send_mail')
    except PeriodicTask.DoesNotExist:
        PeriodicTask.objects.create(
            crontab=schedule,
            name='add device send_mail',
            task='celery_tasks.device.tasks.send_email',
        )


@shared_task
def send_email():
    conn = get_redis_connection("default")
    device = Fa.objects.filter()
    for f in device:

        #work 分布式锁
        if conn.setnx(f.id, 1):
            conn.expire(f.id, 60 * 60 * 3)
        else:
            continue
        print("111111111")
