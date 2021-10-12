#!/usr/bin/python3
""" in this module it implement a method to return an object
    represented by JSON string
"""


import json


def from_json_string(my_str):
    """This function that returns an object (Python data
    structure) represented by a JSON string:
    Arguments:
        my_str {[str]} -- [description]
    """
    return json.loads(my_str)
