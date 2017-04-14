#!/usr/bin/python3

with open('name_list') as f:
    content = f.readlines()

content = [x.strip() for x in content]

print(content)
