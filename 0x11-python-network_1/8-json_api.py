#!/usr/bin/python3
""" Task 8 """
import requests
from sys import argv

if __name__ == "__main__":
    q = ""
        if len(argv) == 2:
                url = "http://0.0.0.0:5000/search_user"
                        obj = {'q': q}
                                req = requests.post(url, obj)
                                        try:
                                                    req = requests.post(url, obj)
                                                                if "id" in req.__dict__ and name in req.__dict__:
                                                                                print("["+str(req.get('id'))+"]
                                                                                "+str(req.get('name')))
                                                                                            else:
                                                                                                            print("No
                                                                                                            result")
                                                                                                                    except:
                                                                                                                                print("Not
                                                                                                                                a
                                                                                                                                valid
                                                                                                                                JSON")
                                                                                                                                    else:
                                                                                                                                            print("No
                                                                                                                                            result")
