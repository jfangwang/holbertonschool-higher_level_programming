#!/usr/bin/python3
""" Task 9 """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        repo = argv[1]
        user = argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
        r = requests.get(url).json()
        count = 0
        for item in r:
            if count < 10:
                count += 1
                print(str(item['sha'])+": "+item['commit']['author']['name'])
