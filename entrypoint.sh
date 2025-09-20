#!/bin/sh

# Exit on error
set -e

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "test"
password = "imrandell"
email = "test@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created: username=test, password=imrandell")
else:
    print("Superuser 'test' already exists.")
EOF

echo "Starting Django server..."
exec "$@"
