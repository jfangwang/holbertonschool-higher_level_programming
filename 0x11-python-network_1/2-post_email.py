#!/usr/bin/python3
""" Task 1 """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 3:
        url = argv[1]
        email = argv[2]
        values = {'email': email}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
