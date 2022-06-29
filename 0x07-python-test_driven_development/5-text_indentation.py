#!/usr/bin/python3
"""
A module with a function that prints a text with
2 new lines after each of these characters: '.',
'?' and ':'
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'

    Args:
        text (str)

    Raises:
        TypeError: if text is not a string
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")

    text = " ".join(text.split())
    ltext = list(text)

    for i in range(len(ltext)):
        if ltext[i] == '.' and ltext[i + 1] == ' ':
            ltext[i] = '.\n\n'
            ltext[i + 1] = ''
        elif ltext[i] == '.' and ltext[i + 1] != ' ':
            ltext[i] = '.\n\n'
        if ltext[i] == '?' and ltext[i + 1] == ' ':
            ltext[i] = '?\n\n'
            ltext[i + 1] = ''
        elif ltext[i] == '?' and ltext[i + 1] != ' ':
            ltext[i] = '?\n\n'
        if ltext[i] == ':' and ltext[i + 1] == ' ':
            ltext[i] = ':\n\n'
            ltext[i + 1] = ''
        elif ltext[i] == ':' and ltext[i + 1] != ' ':
            ltext[i] = ':\n\n'

    lstr = ''.join(ltext)
    print("{:s}".format(lstr), end="")
