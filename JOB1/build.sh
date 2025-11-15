#!/bin/bash
set -o errexit

cd job1

pip install -r ../requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate
