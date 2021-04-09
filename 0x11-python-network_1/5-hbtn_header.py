#!/usr/bin/python3
""" Task 5 """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
