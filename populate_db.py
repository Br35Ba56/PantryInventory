from api.models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

objects = [
    {
        "name": "Squash",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29"
    },
    {
        "name": "Bacon",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29"
    },
    {
        "name": "Bacon",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29"
    },
    {
        "name": "Bacon",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29"
    },
    {
        "name": "Bacon",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29"
    }
]

user = authenticate(username='root', password='root')
for object_ in objects:
    Item(name=object_['name'], quantity_with_unit=object_['quantity_with_unit'], acquisition_date=object_['acquisition_date'], expiration_date=object_['expiration_date'], user_id=user).save()