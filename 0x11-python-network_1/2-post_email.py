#!/usr/bin/python3
"""
A script takes in a URL & an email and displays the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {}
    value['email'] = bytes(sys.argv[2], 'utf-8')
    data = urllib.parse.urlencode(value)
    mail = data.encode('ascii')
    req = urllib.request.Request(url=sys.argv[1], data=mail, method='POST')
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
