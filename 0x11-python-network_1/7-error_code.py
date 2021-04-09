#!/usr/bin/python3
""" Task 7 """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        try:
            req = requests.get(url)
            print(req.text)
        except Exception as e:
            print('Error code: ' + str(e.code))
