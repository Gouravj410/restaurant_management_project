import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')

app = Celery('restaurant_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Run every night at 11:59 PM
app.conf.beat_schedule = {
    'generate-daily-sales-report': {
        'task': 'orders.tasks.generate_sales_report',
        'schedule': crontab(hour=23, minute=59),
    },
}
