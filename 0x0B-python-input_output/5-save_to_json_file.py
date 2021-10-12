#!/usr/bin/python3
"""[summary]"""


import json


def save_to_json_file(my_obj, filename):
    """[summary]
    Arguments:
        my_obj {[type]} -- [description]
        filename {[type]} -- [description]
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
