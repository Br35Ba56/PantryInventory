#!/bin/bash
source /opt/vagrant/python/env/bin/activate
cd /vagrant/PantryInventory && python /vagrant/PantryInventory/manage.py create_group
