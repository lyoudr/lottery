#!/bin/sh

# Run collectstatic to collect all static files
python manage.py collectstatic --noinput

# Start Gunicorn (WSGI server)
gunicorn --bind 0.0.0.0:8000 lottery.wsgi