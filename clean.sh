#!/bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

mysql -u foo -pbar < clean_db.sql
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser