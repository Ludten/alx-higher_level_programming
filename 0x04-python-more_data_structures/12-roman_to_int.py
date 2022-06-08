#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and (isinstance(roman_string, str)) is True:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
        number = 0
        roman_string = roman_string.replace(
            "IV", "IIII").replace("IX", "VIIII")
        roman_string = roman_string.replace(
            "XL", "XXXX").replace("XC", "LXXXX")
        roman_string = roman_string.replace(
            "CD", "CCCC").replace("CM", "DCCCC")
        for char in roman_string:
            number += roman[char]
        return number
    return 0
