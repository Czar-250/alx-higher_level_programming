#!/usr/bin/python3
'''This module defines a function that adds 2 integers'''


def add_integer(a, b=98):
    '''Returns the addition of two integers else
    throw an error if a and b are neither an integer nor a flot'''

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
