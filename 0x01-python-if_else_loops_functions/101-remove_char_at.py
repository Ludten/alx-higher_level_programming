#!/usr/bin/python3
def remove_char_at(str, n):
    result = ''
    if n >= len(str) or n < 0:
        return str
    for char in str:
        if char != str[n]:
            result += char
    return result
