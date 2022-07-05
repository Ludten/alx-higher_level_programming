#!/usr/bin/python3
"""
A module on log parsing
"""

import sys


def print_stat(filesize, statcode):
    """
    A function for printing the logs
    """
    print("File size: {:d}". format(filesize))
    for k, v in sorted(statcode.items()):
        if v > 0:
            print("{:s}: {:d}".format(k, v))


if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stat(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stat(size, status_codes)

    except KeyboardInterrupt:
        print_stat(size, status_codes)
        raise
