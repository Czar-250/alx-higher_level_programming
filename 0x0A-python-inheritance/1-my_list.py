#!/usr/bin/python3
"""This module inherits from a list class"""


class MyList(list):
    '''A sub class of list'''

    def print_sorted(self):
        '''A public instance method that prints the list,
        but sorted (ascending sort)'''

        print(sorted(self))
