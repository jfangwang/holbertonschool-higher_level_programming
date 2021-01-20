#!/usr/bin/python3
"""task 5"""
import json


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, mode='w', encoding='utf-8') as w:
        return json.dump(my_obj, w)
