#!/usr/bin/python3
"""This class represents a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''Importing a super class BaseGeometry'''


class Rectangle(BaseGeometry):
    '''A subclass of BaseGeometry'''

    def __init__(self, width, height):
        '''Initialising an instance'''

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
