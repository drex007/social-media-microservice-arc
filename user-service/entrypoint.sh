#!/bin/sh
set -e #Cancels the running of scripts incase of any error

python manage.py makemigrations
python manage.py migrate  --no-input
python manage.py collectstatic --no-input
gunicorn users.wsgi:application --bind 0.0.0.0:8000


