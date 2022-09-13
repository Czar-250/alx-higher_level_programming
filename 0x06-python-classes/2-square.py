#!/usr/bin/python3

'''This represents a square module'''


class Square:
    '''represents a class square.
    Private instance attribute: size
    Instantiation with optional size'''

    def __init__(self, size=0):
        '''Initializing square object'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
