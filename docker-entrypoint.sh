#!/bin/sh
flask db upgrade
gunicorn --config /app/gunicorn_config.py app.wsgi:app
