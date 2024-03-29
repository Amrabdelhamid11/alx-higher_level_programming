#!/usr/bin/python3
"""
This module has a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "wt") as f:
        return f.write(text)
