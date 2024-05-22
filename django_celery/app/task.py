import logging
from time import sleep

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def sub(x, y):
    sleep(10)
    result = x - y
    logger.info(f"Subtraction result: {result}")
    return result


@shared_task
def add(x, y):
    sleep(20)
    result = x + y
    logger.info(f"Addition result: {result}")
    return result


@shared_task
def scad():
    return "Scheduling"
