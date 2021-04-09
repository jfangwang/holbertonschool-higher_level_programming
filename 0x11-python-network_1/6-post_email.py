#!/usr/bin/python3
""" Task 6 """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        email = argv[2]
        dic = {'email': email}
        req = requests.post(url, dic)
        print(req.text)
