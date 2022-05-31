#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = int(repr(number)[-1])
    else:
        last_digit = int(repr(number)[-1])
        last_digit *= -1
    return last_digit
