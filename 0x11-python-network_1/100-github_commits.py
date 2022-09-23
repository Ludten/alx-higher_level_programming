#!/usr/bin/python3
"""
A script that list 10 commits (from the most recent to oldest) of the
repository “rails” by the user
"""


def myFunc(e):
    """a function that returns date"""
    return e['commit']['author']['date']


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits\
?per_page=10&order=asc&sort=committer-date'.
        format(sys.argv[2], sys.argv[1])
    )
    body = r.json()
    # body.sort(reverse=True, key=myFunc)
    for items in body:
        if 'sha' in items:
            print('{}: {}'.format(items['sha'],
                  items['commit']['author']['name']))
        else:
            print(None)
