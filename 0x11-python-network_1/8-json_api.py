#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    value = {}
    if len(sys.argv) > 1:
        value['q'] = sys.argv[1]
    else:
        value['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        body = r.json()
        if body and body != {}:
            print('[{}] {}'.format(body['id'], body['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
