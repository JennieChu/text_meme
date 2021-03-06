#!/usr/bin/python3
"""
generate JSON file for information on all memes
"""
import json


with open('meme_list') as f:
    content = f.readlines()

content = [x.strip() for x in content]

image_json = []
prefixurl = "../static/images/memages/"


for x in content:
    new_dict = {}
    validurl = x
    new_dict["url"] = prefixurl + validurl
    new_dict["name"] = x.replace('+', ' ')
    image_json.append(new_dict)

with open("memages.json", mode='w') as f:
    f.write(json.dumps(image_json))
