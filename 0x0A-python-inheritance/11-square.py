#!/usr/bin/python3
"""This module represents a class Square"""

Rectangle = __import__('9-rectangle').Rectangle
'''importing the module'''


class Square(Rectangle):
    '''this class inherits from Rectangle'''

    def __init__(self, size):
        '''Initialising an instance'''

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        '''Implementing the area method'''

        return self.__size ** 2

    def __str__(self):
        '''returns the square description:
        [Square] <width>/<height>'''

        return "[Square] {}/{}".format(self.__size, self.__size)
