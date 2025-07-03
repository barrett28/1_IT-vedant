import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"  # ✅ trailing slash important

data = {
    'name': 'abc',
    'roll': 101,
    'city': 'Mumbai'
}

headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data, headers=headers)

data = r.json()

print(data)
