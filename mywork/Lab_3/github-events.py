#!/bin/python3
import os
import json
import requests
GHUSER = os.getenv('GITHUB_USER')
print(GHUSER)
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)
print(r)
