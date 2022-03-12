import json
import requests

r = requests.get('http://192.168.1.12:8160', stream=True)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('lintel')
        print(json.loads(decoded_line))
