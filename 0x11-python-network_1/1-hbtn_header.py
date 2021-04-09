#!/usr/bin/python3
""" Task 1 """
import urllib.request
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 2:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            html = response.read()
            info = type(html)
            print(response.getheader('X-Request-Id'))
