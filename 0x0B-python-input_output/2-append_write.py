#!/usr/bin/python3
"""Module 2-append_write appends a string
at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    '''filename: name of the file
    text: text to be appended
    returns: the number of characters added'''

    with open(filename, "a", encoding="utf_8") as f:
        return f.write(text)
