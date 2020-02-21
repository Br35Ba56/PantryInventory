#!/bin/bash

if [[ -f /vagrant/PantryInventory/PanInv-sqlite ]]
then
    rm -f /vagrant/PantryInventory/PanInv-sqlite
fi
python /vagrant/PantryInventory/manage.py makemigrations
python /vagrant/PantryInventory/manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'admin@myproject.com', 'root')" | python /vagrant/PantryInventory/manage.py shell