from celery import shared_task
import time

import uuid


@shared_task
def heavy_task(params: dict):
    time.sleep(10)
    return uuid.uuid4()
