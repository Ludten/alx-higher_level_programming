#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        s = 0
        for i in my_list:
            s += (i[0] * i[1])
        w = 0
        for x in my_list:
            w += x[1]
        return s / w
    return 0
