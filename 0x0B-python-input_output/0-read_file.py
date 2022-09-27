#!/usr/bin/python3
"""Module 0-read_file reads a text file
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    '''filename: is name of the file'''
    with open(filename, encoding="UTF8") as f:
        read_text = f.read()
        print(read_text, end="")
