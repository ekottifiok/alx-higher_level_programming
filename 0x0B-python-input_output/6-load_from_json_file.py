#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
from json import load


def load_from_json_file(filename):
    """read from a file a json

    Args:
        filename (str): file name

    Returns:
        str: the json read from the file
    """
    with open(filename, 'r') as f:
        return load(f)
