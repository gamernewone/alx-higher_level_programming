#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''Return the sum of 2 tuples'''

    # Checks
    if len(tuple_a) < 2:
        while len(tuple_a) < 2:
            tuple_a += (0, )

    if len(tuple_b) < 2:
        while len(tuple_b) < 2:
            tuple_b += (0, )

    # The sum
    tuple_c = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return (tuple_c)
