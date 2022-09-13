#!/usr/bin/python3

'''Square class module'''


class Square:
    '''class Square that defines a square
    Private instance attribute: size
    Instantiation with size (no type/value verification)'''

    def __init__(self, size):
        '''initializing the square object'''
        self.__size = size
