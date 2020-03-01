import csv

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Item
from faker import Faker

FOOD = ['Bacon', 'Eggs', 'Milk', 'Peanut Butter', 'Jelly', 'Bread', 'Ham', 'Turkey', 'Chedder', 'Water Bottle']
QUANTITYUNIT = ['.75 Lb', '1/2 Quart', '1 Gallon', '3 Cups', '5 Teaspoon', '2 Tablespoons', '8 fl oz', '4 Pints', '.25 L', '7 Ounce']

class Command(BaseCommand):
    help = 'Adds randomized data to the backend'
    def handle(self, *args, **options):
        fake = Faker()
        my_group = Group.objects.get(name='api_user_group')
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for _ in range(0,15):
                tempname=fake.first_name()+fake.last_name()
                temppass=fake.word(ext_word_list=None)+fake.word(ext_word_list=None)
                new_user = User.objects.create(username=tempname, password=temppass)
                my_group.user_set.add(new_user)
                writer.writerow([tempname, temppass])
                for _ in range(0,500):
                    Item.objects.create(name=fake.word(ext_word_list=FOOD), user_id=new_user, quantity_with_unit=fake.word(ext_word_list=QUANTITYUNIT), acquisition_date=fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"), expiration_date=fake.date_between(start_date='today', end_date='+1d').strftime("%Y-%m-%d"))
                for _ in range(0,500):
                    Item.objects.create(name=fake.word(ext_word_list=FOOD), user_id=new_user, quantity_with_unit=fake.word(ext_word_list=QUANTITYUNIT), acquisition_date=fake.date_between(start_date='-7d', end_date='-1d').strftime("%Y-%m-%d"), expiration_date=fake.date_between(start_date='+1d', end_date='+7d').strftime("%Y-%m-%d"))
                for _ in range(0,500):
                    Item.objects.create(name=fake.word(ext_word_list=FOOD), user_id=new_user, quantity_with_unit=fake.word(ext_word_list=QUANTITYUNIT), acquisition_date=fake.date_between(start_date='-1d', end_date='today').strftime("%Y-%m-%d"), expiration_date=fake.date_between(start_date='+7d', end_date='+1y').strftime("%Y-%m-%d"))