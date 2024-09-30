#!/usr/bin/env bash

set -e

chown www-data:www-data /var/log

python manage.py migrate
# python manage.py collectstatic --noinput
# python manage.py compilemessages -l en -l ru

uwsgi --strict --ini /opt/app/uwsgi.ini
