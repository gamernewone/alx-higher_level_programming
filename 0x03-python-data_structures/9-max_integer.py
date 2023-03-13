#!/usr/env/python3

def max_integer(my_list=[]):
    '''Return the max integer in a list'''

    if (len(my_list) == 0):
        return (None)

    max = 0

    for number in my_list:
        if number > max:
            max = number
    return max
