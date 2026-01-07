import requests
import json

URL = "http://127.0.0.1:8000/student/create/"

data={
    "name":"Alice",
    "roll_number":101,
    "age":20,
    "city":"New York"
}

json_data=json.dumps(data)

response = requests.post(url=URL, data=json_data)

print(response)