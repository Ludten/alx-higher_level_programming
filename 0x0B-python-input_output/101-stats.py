#!/usr/bin/python3
"""
A module on log parsing
"""

import sys

ln = 0
file_size = 0
sc20 = 0
sc31 = 0
sc40 = 0
sc41 = 0
sc43 = 0
sc44 = 0
sc45 = 0
sc50 = 0
if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                ln += 1
                p_line = line.split(" ")
                stat_code = int(p_line[-2])
                file_size += int(p_line[-1])
                if stat_code == 200:
                    sc20 += 1
                elif stat_code == 301:
                    sc31 += 1
                elif stat_code == 400:
                    sc40 += 1
                elif stat_code == 401:
                    sc41 += 1
                elif stat_code == 403:
                    sc43 += 1
                elif stat_code == 404:
                    sc44 += 1
                elif stat_code == 405:
                    sc45 += 1
                elif stat_code == 500:
                    sc50 += 1
                if (ln % 10 == 0):
                    print("File size: {:d}". format(file_size))
                    if sc20 > 0:
                        print("200: {:d}".format(sc20))
                    if sc31 > 0:
                        print("301: {:d}".format(sc31))
                    if sc40 > 0:
                        print("400: {:d}".format(sc40))
                    if sc41 > 0:
                        print("401: {:d}".format(sc41))
                    if sc43 > 0:
                        print("403: {:d}".format(sc43))
                    if sc44 > 0:
                        print("404: {:d}".format(sc44))
                    if sc45 > 0:
                        print("405: {:d}".format(sc45))
                    if sc50 > 0:
                        print("500: {:d}".format(sc50))
            except KeyboardInterrupt:
                pass

    except KeyboardInterrupt:
        print("File size: {:d}". format(file_size))
        if sc20 > 0:
            print("200: {:d}".format(sc20))
        if sc31 > 0:
            print("301: {:d}".format(sc31))
        if sc40 > 0:
            print("400: {:d}".format(sc40))
        if sc41 > 0:
            print("401: {:d}".format(sc41))
        if sc43 > 0:
            print("403: {:d}".format(sc43))
        if sc44 > 0:
            print("404: {:d}".format(sc44))
        if sc45 > 0:
            print("405: {:d}".format(sc45))
        if sc50 > 0:
            print("500: {:d}".format(sc50))
