#!/usr/bin/python3
"""Module 5-save_to_json_file writes an Object
to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    '''my_obj: json representation
    filename: name of the file for text to be saved'''

    with open(filename, "w") as f:
        json.dump(my_obj, f)
