from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Item
from faker import Faker

class Command(BaseCommand):
    help = 'Adds randomized data to the backend'
    
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(0,10):
            new_user = User.objects.create(username=fake.first_name()+fake.last_name(), password=fake.word(ext_word_list=None)+fake.word(ext_word_list=None))
            new_user.save()
            for _ in range(0,10):
              Item.objects.create(name=fake.word(ext_word_list=None), user_id = new_user, quantity_with_unit=fake.word(ext_word_list=None), acquisition_date=fake.date(pattern='%Y-%m-%d', end_datetime=None), expiration_date=fake.date(pattern='%Y-%m-%d', end_datetime=None))  