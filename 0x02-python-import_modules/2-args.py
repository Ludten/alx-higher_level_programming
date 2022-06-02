#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(len(sys.argv) - 1, "arguments.")
    elif len(sys.argv) > 1:
        print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
