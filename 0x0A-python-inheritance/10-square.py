#!/usr/bin/python3
"""This module represents a class Square
that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
'''Importing the inherited class'''


class Square(Rectangle):
    '''A subclass of Rectangle'''

    def __init__(self, size):
        '''Initialising an instance'''

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        '''Implementing the area method'''

        return self.__size * self.__size
