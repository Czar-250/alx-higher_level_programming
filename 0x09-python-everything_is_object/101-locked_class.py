#!/usr/bin/python3
'''Represents a locked class module'''


class LockedClass:
    '''Initializing data'''
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
