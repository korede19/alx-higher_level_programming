#!/usr/bin/python3
"""[summary]
"""


from sys import argv
from os import path


save_from_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
list_argv = argv[1:]
if path.exists(filename):
    object_py = load_from_json(filename)
else:
    object_py = []
object_py.extend(list_argv)
save_from_json(object_py, filename)
