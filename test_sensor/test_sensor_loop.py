import os
import json
import requests
import uuid

tok = os.environ.get("AUTH_TOKEN")
print(f"TOKEN: {tok}")
uuid_str = str(uuid.uuid4())
print(f"UUID: {uuid}")

create_data = {
    "kind": "temperature",
    "name": "tester2",
    "unit": "F",
    "uuid": uuid_str
}

data_json = json.dumps(create_data)

resp = requests.post('http://localhost:8000/sensors/', headers={'Authorization': f'token {tok}'}, json=create_data)

if resp.status_code != 200:
    print(resp.status_code)
    print(resp.json())
        