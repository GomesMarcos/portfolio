#!/bin/bash

python manage.py migrate
echo "\nMigrations applied successfully.\n"

echo "\nLoading static files...\n"
/app/static/css/tailwindcss -i /app/static/css/input.css -o /app/static/css/output.css --minify
rm -rf /app/productionfiles/*
python manage.py collectstatic --noinput
echo "\nStatic files loaded successfully.\n"

echo "\nRunning server...\n"

gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
