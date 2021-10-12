#!/usr/bin/python3
""" In this module it create a method to appends at string
    at the end of a tex file
"""


def append_write(filename="", text=""):
    """This function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added:
    Arguments:
        filename {str} -- This is the file to read(default: {""})
        text {str} -- text to add at the end of the file
        (default: {""})
    """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
