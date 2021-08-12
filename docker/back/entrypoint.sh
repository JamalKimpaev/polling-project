#!/bin/sh -evx

python3 /project/manage.py migrate
python3 /project/manage.py collectstatic --noinput

exec "$@"
