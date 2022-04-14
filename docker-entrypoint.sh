#!/bin/sh
cd app/ && flask db upgrade
cd ../ && gunicorn --config /app/gunicorn_config.py app.wsgi:viewgerapp
