#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for i in range(len(new_string)):
        if new_string[i] == 'c' or new_string[i] == 'C':
            new_string[i] = ''
    n_string = "".join(new_string)
    return n_string
