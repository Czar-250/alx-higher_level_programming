#!/usr/bin/python3
"""Module 1-write_file writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    '''filename: name of the file
    text: text to be written'''

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
