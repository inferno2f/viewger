#!/bin/sh
flask db upgrade
flask pull_gitlab_data
gunicorn --config /app/gunicorn_config.py app.wsgi:app
