import pytest
import requests
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import os 
import random
import json
import copy
from faker import Faker
fake = Faker()
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


food = ['Bacon', 'Eggs', 'Milk', 'Peanut Butter', 'Jelly', 'Bread', 'Ham', 'Turkey', 'Chedder', 'Water Bottle']
quantity_with_unit = ['.75 Lb', '1/2 Quart', '1 Gallon', '3 Cups', '5 Teaspoon', '2 Tablespoons', '8 fl oz', '4 Pints', '.25 L', '7 Ounce']


def test_get_items(r):
    assert r.status_code == 200

def test_get_token(token):
    assert 'access_token' in token

def test_modify_item(item, token):
    url = "http://localhost:8000/item"

    payload = item
    print(item)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer mYF7Wzeo6qBDsYBGgSl3EztMS1JHFS'
    }

    r = requests.request("POST", url, headers=headers, data = payload)
    assert r.status_code == 200


def test_revoke_token(token, client_id, client_secret):
    url = "http://localhost:8000/o/revoke_token/"

    payload = 'token=' + token['access_token'] +'&client_id='+ client_id+ '&client_secret=' + client_secret
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.request("POST", url, headers=headers, data = payload)
    assert r.status_code == 200

    

client_id = "HyJ86HsVaO2Lsh9mDzPN8M3S0cuVyfdpf3JbhcoG"
client_secret = "thzut55oYWlDt1rjesqMS9mbKpueY1beG364ZYDxW64Ij8DGxldrX4ULjdKxZYGgT3Cm7KI5G0KcDU73hTizbyAu5czzSjyFvVF5GVfLm6rOHNkBAqTAhr7QIH76rity"
token_url = 'http://localhost:8000/o/token/'

item_url = 'http://localhost:8000/item'

user_file = './users.csv'
userlist = []
with open(user_file, 'r') as file:
    for line in file:
        username, password = line.split(',')
        userlist.append((username, password.strip('\n')))
        
for user in userlist:
    oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
    token = oauth.fetch_token(token_url=token_url,
        username=user[0], password=user[1], client_id=client_id,
        client_secret=client_secret)
    
    #Test the token was retrieved 
    test_get_token(token)
    
    #Test getting Items with search
    r = oauth.get(item_url + '?name=' + food[random.randint(0, (len(food) - 1))])
    test_get_items(r)

    #Test getting Items without search
    r = oauth.get(item_url)    
    test_get_items(r)

    #Test Modify Items
    for item in copy.deepcopy(r.json()):
        name=fake.word(ext_word_list=food)
        quantity_with_unit=fake.word(ext_word_list=quantity_with_unit)
        acquisition_date=fake.date_between(start_date='-1d', end_date='today').strftime("%Y-%m-%d")
        expiration_date=fake.date_between(start_date='+7d', end_date='+1y').strftime("%Y-%m-%d")
        item['name'] = name
        item['quantity_with_unit'] = quantity_with_unit
        item['acquisition_date'] = acquisition_date
        item['expiration_date'] = expiration_date
        #del item['id']
        del item['user_id']
        print(item)
        test_modify_item(item, token)
        break

    #Test Revoke Token

    test_revoke_token(token, client_id, client_secret)