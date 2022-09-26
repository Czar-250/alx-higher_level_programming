#!/usr/bin/python3
"""This module represents a class MyInt"""


class MyInt(int):
    '''This module inherits from class int'''

    def __eq__(self, other):
        '''defines Equality(== operator)'''

        return int.__ne__(self, other)

    def __ne__(self, other):
        '''Defines Inequarinty(!= operator)'''

        return int.__eq__(self, other)
