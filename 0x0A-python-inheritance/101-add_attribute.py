#!/usr/bin/python3
"""This module represents a function"""


def add_attribute(self, att, value):
    '''adds a new attribute to an object if it’s possible'''

    if hasattr(self, '__dict__'):
        setattr(self, att, value)
    else:
        raise TypeError("can't add new attribute")
