#!/usr/bin/python3
"""returns the dictionary description with
simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    '''obj is an instance of a Class
    All attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean'''

    return obj.__dict__
