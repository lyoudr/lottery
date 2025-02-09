import os
from celery import Celery
from celery.schedules import crontab

# Set default Django settings moduel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottery.settings')

app = Celery('lottery')

# Load task modules from all registered Django apps
app.conf.update(
    # Celery
    CELERY_BROKER_URL = "pyamqp://guest@localhost//", # RabbitMQ
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_TASK_ACKS_LATE = True,
    CELERY_BEAT_SCHEDULE = {
        'get_lottery_data': {
            'task': 'get_lottery_data',
            'schedule': crontab(minute="*/1"), #crontab(minute=0, hour=0, day_of_month=1)
        }
    },
    CELERY_QUEUES = {
        'lonquery_pq': {
            'exchange': 'longquery_pq',
            'exchange_type': 'direct',
            'routing_key': 'longquery_pq',
        }
    }
)

# Autodiscover tasks in installed apps
app.autodiscover_tasks()