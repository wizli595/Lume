#!/bin/bash

# ----------------------------------------
# LUME Django Startup Script
# Supports SQLite/MySQL, Superuser auto-create using .env
# ----------------------------------------

echo " Starting LUME Django project setup..."


if [ -f .env ]; then
    echo "📦 Loading environment variables from .env"
    export $(grep -v '^#' .env | xargs)
else
    echo "⚠️  .env file not found. Exiting."
    exit 1
fi


if [[ "$1" == "--reset-db" && -f db.sqlite3 ]]; then
    echo "⚠️  Resetting: Deleting existing SQLite database..."
    rm -f db.sqlite3
fi


echo "🔧 Running database migrations..."
poetry run python manage.py migrate

echo "👤 Checking for superuser '${DJANGO_SUPERUSER_USERNAME}'..."
poetry run python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f" Created superuser: {username}")
else:
    print(f" Superuser '{username}' already exists.")
EOF

echo "Starting Django development server at http://127.0.0.1:8000/"
poetry run python manage.py runserver
