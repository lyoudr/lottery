#!/bin/sh

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn (WSGI server)
gunicorn --bind 0.0.0.0:8000 lottery.wsgi