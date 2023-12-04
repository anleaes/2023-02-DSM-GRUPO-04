#!/bin/bash -ex
DJANGO_ENV=$DJANGO_ENV COLLECT_STATIC=1 python3 manage.py collectstatic --noinput 
python3 manage.py migrate
gunicorn --workers 1 --threads 8 --timeout 0 aigo.wsgi:application