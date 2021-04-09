#!/usr/bin/python3
""" Task 9 """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        url = "https://api.github.com/user"
        username = argv[1]
        password = argv[2]
        r = requests.get(url, auth=(username, password)).json()
        print(r.get('id'))
