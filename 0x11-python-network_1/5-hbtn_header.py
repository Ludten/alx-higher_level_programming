#!/usr/bin/python3
"""
A script takes in a URL and displays the value of the X-Request-Id variable
found in the header of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    header = r.headers.get('X-Request-Id')
    print(header)
