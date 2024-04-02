#!/bin/bash

# Start database migrations
python manage.py migrate

# Start Gunicorn server
gunicorn desvio.wsgi:application -w 4 -b 0.0.0.0:8000
