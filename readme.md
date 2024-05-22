## to Install

## pip install -r requirements.txt

## start the amazing redis server

## sudo service redis-server start

## Worker command

## celery -A django_celery worker -l info

## Beat command

## celery -A django_celery beat -l INFO --scheduler

## celery -A django_celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
