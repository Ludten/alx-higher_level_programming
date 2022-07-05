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
    for k, v in statcode.items():
        if v > 0:
            print("{:s}: {:d}".format(k, v))


ln = 0
file_size = 0
stat_code = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
if __name__ == "__main__":
    try:
        for line in sys.stdin:
            ln += 1
            p_line = line.split(" ")
            if p_line[-2] in stat_code:
                stat_code[p_line[-2]] += 1
            file_size += int(p_line[-1])
            if (ln % 10 == 0):
                print_stat(file_size, stat_code)
    except KeyboardInterrupt:
        print_stat(file_size, stat_code)
