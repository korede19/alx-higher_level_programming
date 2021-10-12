#!/usr/bin/python3
"""In this module it create a function count line munber
   of a file
"""


def number_of_lines(filename=""):
    """This function that returns the number of lines of
        a text file
    Arguments:
        filename {str} -- Name of the file to read (default: {""})
    """
    line_numbers = 0
    with open(filename, mode='r', encoding="utf-8") as my_file:
        while (my_file.readline() != ''):
            line_numbers += 1
    return line_numbers
