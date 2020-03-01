import csv

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Item
from faker import Faker

class Command(BaseCommand):
    help = 'Adds randomized data to the backend'
    def handle(self, *args, **options):
        fake = Faker()
        my_group = Group.objects.get(name='api_user_group')
        with open('userstest.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for _ in range(0,150):
                tempname=fake.first_name()+fake.last_name()
                temppass=fake.word(ext_word_list=None)+fake.word(ext_word_list=None)
                new_user = User.objects.create(username=tempname, password=temppass)
                my_group.user_set.add(new_user)
                writer.writerow([tempname, temppass])