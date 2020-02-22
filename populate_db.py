
import requests
import json 


url = "http://127.0.0.7:8000/item"

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
        "expiration_date": "2020-02-29",
    },
    {
        "name": "Bacon",
        "quantity_with_unit": "2 lb",
        "acquisition_date": "2020-02-22",
        "expiration_date": "2020-02-29",
    }
]


headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer dTZexYz1HZiIVsKAkcE1xicv0EjZtd'#UPDATE WITH POSTMAN VALUE
}

for object_ in objects:
    response = requests.request("POST", url, headers=headers, data=json.dumps(object_))
    print(response.text.encode('utf8'))


