#!/bin/bash
mkdir -p /app/data
python manage.py migrate
python manage.py runserver 0.0.0.0:${PORT:-8000}
