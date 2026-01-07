import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    print(r.status_code)

# get_data()

def post_data():
    data={
        'name':'Ravi Kumar',
        'roll_number':104,
        'age':23,
        'city':'Mumbai'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    print(r.status_code)
    print(r.json())

# post_data()

def update_data():
    data={
        'id':3,
        'name':'Rahul Sharma',
        'roll_number':105,
        'age':24,
        'city':'Chennai'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    print(r.status_code)
    print(r.json())

# update_data()

def delete_data():
    data={
        'id':3
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    print(r.status_code)
    print(r.json())

delete_data()