#!/usr/bin/python3
"""task 6"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, encoding='utf-8') as w:
        return json.load(w)
