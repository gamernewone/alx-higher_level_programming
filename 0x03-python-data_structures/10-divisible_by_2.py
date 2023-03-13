#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list'''

    new_lst = [True if item % 2 == 0 else False for item in my_list]

    return (new_lst)
