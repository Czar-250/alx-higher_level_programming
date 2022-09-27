#!/usr/bin/python3
"""Module 4-from_json_string returns an object
(Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    '''my_str:json string'''

    return json.loads(my_str)
