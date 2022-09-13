#!/usr/bin/python3

'''This module represents a class Square module'''


class Square:
    '''Represents a square class
    Private instance attribute: size
    Instantiation with optional size'''
    def __init__(self, size=0):
        '''Initializing square object'''
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns the current square area'''
        return self.__size ** 2
