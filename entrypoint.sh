#!/bin/sh

# Exit on error
set -e

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting Django server..."
exec "$@"