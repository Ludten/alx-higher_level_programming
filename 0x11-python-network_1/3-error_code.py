#!/usr/bin/python3
"""
A script takes in a URL and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
