#!/usr/bin/python3
"""
A script takes in a URL & an email and displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    value = {}
    value['email'] = sys.argv[2]
    r = requests.post(sys.argv[1], data=value)
    print(r.text)
