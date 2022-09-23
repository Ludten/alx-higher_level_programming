#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print(None)
