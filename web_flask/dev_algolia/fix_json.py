#!/usr/bin/python3
"""
fix JSON file
"""
import json

with open('memages.json') as f:
    content = json.load(f)

for i in content:
    i['url'] = i['url'][3:]
    i['url'] = i['url'].replace('memages/', '')
    print(i)

with open('newmemages.json', mode='w') as f:
    f.write(json.dumps(content))
