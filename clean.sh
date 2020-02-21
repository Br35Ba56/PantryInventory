#!/bin/bash

if [[ -f /vagrant/PantryInventory/PanInv-sqlite ]]
then
    rm -f /vagrant/PantryInventory/PanInv-sqlite
fi
cd /vagrant/PantryInventory/ && python manage.py makemigrations && python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'admin@myproject.com', 'root')" | python /vagrant/PantryInventory/manage.py shell