#!/usr/bin/python3
"""
function returns an object (Python data structure)
represented by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """returns a string

    Args:
        my_obj (str): jsonified str

    Returns:
        str: the string to be jsonified
    """
    return loads(my_str)
