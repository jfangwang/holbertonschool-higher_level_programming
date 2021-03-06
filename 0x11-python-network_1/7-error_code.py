#!/usr/bin/python3
""" Task 7 """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        req = requests.get(url)
        if req.status_code >= 400:
            print("Error code: " + str(req.status_code))
        else:
            print(req.text)
