import json
from urllib.request import urlopen


myObj = '''{
  "name":"John",
  "age":30,
  "cars": {
    "car1":"Ford",
    "car2":"BMW",
    "car3":"TESLA"
  }
}'''

data = json.loads(myObj)

with open('new_state_json,json', 'w') as f:
    json.dump(data, f, indent=2)

with urlopen("https://api.exchangeratesapi.io/latest") as response:
    source = json.loads(response.read().decode('utf-8'))

print(source["rates"])

for rate in source["rates"]:
    print('{} : {}'.format(rate, source["rates"][rate]))

with open('exchange_rate.csv', 'w') as f:
    json.dump(source, f, indent=2)
