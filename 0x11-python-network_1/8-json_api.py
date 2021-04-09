#!/usr/bin/python3
""" Task 8 """
import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) == 2:
        url = "http://0.0.0.0:5000/search_user"
        q = argv[1]
        obj = {'q': q}
        try:
            req = requests.post(url, data=obj).json()
            if req.get('id') is not None and req.get('name') is not None:
                print("["+str(req.get('id'))+"] "+str(req.get('name')))
            else:
                print("No result")
        except:
            print("Not a valid JSON")
    else:
        print("No result")
