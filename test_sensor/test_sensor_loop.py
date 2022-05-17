import os
import json
import requests
import datetime
import uuid

tok = os.environ.get("AUTH_TOKEN")
print(f"TOKEN: {tok}")
uuid_str = str(uuid.uuid4())
print(f"UUID: {uuid_str}")

create_data = {
    "kind": "temperature",
    "name": uuid_str[:10],
    "unit": "F",
    "uuid": uuid_str
}

url = lambda endp: f'http://localhost:8000/{endp}/'


data_json = json.dumps(create_data)
head = {'Authorization': f'token {tok}'}

print(url('sensors'))

resp = requests.post(url('sensors'), headers=head, json=create_data)

if resp.status_code != 200:
    print(resp.status_code)
    print(resp.json())

data = {
    'uuid': uuid_str,
}
for i in range(15):
    data['timestamp'] = datetime.datetime.now().isoformat()
    print(data['timestamp'])
    data['value'] = i
    resp = requests.post(url('sensorvalues'), headers=head, json=data)
    print(resp.status_code)
    print(resp.json())

resp = requests.get(url('sensorvalues'), headers=head)

print(resp.status_code)
print(json.dumps(resp.json(), indent=4))
