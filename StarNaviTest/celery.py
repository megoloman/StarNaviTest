from __future__ import absolute_import

from datetime import timedelta


CELERY_ENABLE_UTC = False
CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_EAGER_PROPAGATES = False

CELERY_BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = None
CELERY_CACHE_BACKEND = None

CELERY_BEAT_SCHEDULE = {
    'post_bot': {
        'task': 'apps.post.tasks.post_bot',
        'schedule': timedelta(hours=1),
    },
}
