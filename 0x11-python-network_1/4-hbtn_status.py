#!/usr/bin/python3
""" Task 4 """
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("\tBody response:")
    print("\t- type: " + str(type(req.text)))
    print("\t- content: " + str(req.text))
