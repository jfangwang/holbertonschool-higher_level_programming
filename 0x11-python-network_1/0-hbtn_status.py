#!/usr/bin/python3
""" Task 0 """
import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read()
    info = type(html)
    utf = html.decode('utf-8')
    print("Body response:")
    print("    - type:" + str(info))
    print("    - content:" + str(html))
    print("    - utf8 content:" + str(utf))
