#!/usr/bin/python3
"""This module represents a subclass Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This class inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''Initializing an instance'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Implementing the area method'''

        return self.__width * self.__height

    def __str__(self):
        '''Returns a rectangle description: [Rectangle] <width>/<height>'''

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
