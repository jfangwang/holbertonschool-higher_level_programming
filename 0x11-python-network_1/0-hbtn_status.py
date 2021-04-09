#!/usr/bin/python3
""" Task 0 """
import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read()
    info = type(html)
    utf = html.decode('utf-8')
    print("Body response:")
    print("\t- type:" + str(info))
    print("\t- content:" + str(html))
    print("\t- utf8 content:" + str(utf))
