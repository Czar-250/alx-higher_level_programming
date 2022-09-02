#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    info: adds all unique integers in a list (only once for each integer).
    '''
    result = sum(set(my_list))
    return result
