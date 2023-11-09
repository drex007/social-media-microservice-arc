#!/bin/sh
set -e 

python manage.py makemigrations
python manage.py migrate  --no-input
python manage.py collectstatic --no-input
# uvicorn chats.asgi:application --bind 0.0.0.0:8003
# uvicorn chats.asgi:application --host 0.0.0.0 --port 8003
python manage.py runserver 0.0.0.0:8003





