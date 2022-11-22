#!/usr/bin/env bash

sudo apt-get install -y python3.10-venv

in_venv=$(python3 -c 'import sys; return sys.prefix != sys.base_prefix')

if ! ${in_venv}; then
  python3 -m venv venv
  source venv/bin/activate
fi

python3 -m pip install -r requirements.txt

cd src

python3 manage.py makemigrations payment --no-input -v 0

python3 manage.py migrate --no-input

if [ "${DJANGO_SUPERUSER_NAME}" ]; then
  python3 manage.py create_admin \
          --username "${DJANGO_SUPERUSER_USERNAME}" \
          --email "${DJANGO_SUPERUSER_EMAIL}" \
          --password "${DJANGO_SUPERUSER_PASSWORD}"
fi

python3 manage.py fill_database --count 10