#!/usr/bin/python3
"""
A script takes in a URL and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
