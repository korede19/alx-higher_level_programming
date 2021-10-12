#!/usr/bin/python3
"""In this module it implemente a method that creates an Object
    from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """This function that creates an Object from a “JSON file”
    Arguments:
        filename {[type]} -- [description]
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        return json.load(my_file)
