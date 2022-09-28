#!/usr/bin/python3
"""function writes an Object to a text file, using a JSON representation
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """writes json to a file

    Args:
        my_obj (str): the string to be written
        filename (str): file name

    """

    with open(filename, "w") as f:
        dump(my_obj, f)
