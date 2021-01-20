#!/usr/bin/python3
"""task 7"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    l = load_from_json_file(filename)
except:
    l = []
for arg in argv[1:]:
    l.append(arg)
save_to_json_file(l, filename)
