#!/usr/bin/python3
"""In this module in implement a method to convert json to str"""


import json


def to_json_string(my_obj):
    """This  function that returns the JSON representation
    of an object (string)
    Arguments:
        my_obj {[type]} -- [description]
    """
    return json.dumps(my_obj)
