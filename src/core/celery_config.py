from celery import Celery
from celery.schedules import crontab

from src.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.autodiscover_tasks(["src.apps.tasks.currency"])

celery_app.conf.beat_schedule = {
    "get_currencies": {
        "task": "src.apps.tasks.currency.download_currencies_task",
        "schedule": crontab(hour=0, minute=33),
        "args": (16, 16),
    },
}
celery_app.conf.timezone = "Europe/Moscow"
