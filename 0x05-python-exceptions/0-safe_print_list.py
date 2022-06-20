#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ctr = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            ctr += 1

    except IndexError:
        pass
    print('')
    return ctr
