#!/bin/sh
flask db upgrade
flask pull-gitlab-data
gunicorn --config /app/gunicorn_config.py app.wsgi:app
