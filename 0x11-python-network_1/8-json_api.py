#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    value = {}
    try:
        value['q'] = sys.argv[1]
    except IndexError:
        value['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    if r.json() and r.json() != {}:
        print('[{}] {}'.format(r.json()['id'], r.json()['name']))
    elif r.json() == {}:
        print('No result')
    else:
        print('Not a valid JSON')
