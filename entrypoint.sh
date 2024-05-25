#!/bin/bash

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Migrate database"
python3 manage.py migrate

echo "Create superuser"
python3 create_superuser.py

echo "Load data"
python3 manage.py loaddata products/fixtures/categories.json
python3 manage.py loaddata products/fixtures/goods.json

echo "Start gunicorn"
exec gunicorn store.wsgi:application --config gunicorn.conf.py --bind 0.0.0.0:8000
