#!/usr/bin/python3
"""creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    '''filename: JSON file'''
    with open(filename) as f:
        return json.load(f)
