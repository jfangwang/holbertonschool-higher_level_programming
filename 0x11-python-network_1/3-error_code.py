#!/usr/bin/python3
""" Task 3 """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 2:
        url = argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                print(html.decode('utf-8'))
        except Exception as e:
            print('Error code: ' + str(e.code))
