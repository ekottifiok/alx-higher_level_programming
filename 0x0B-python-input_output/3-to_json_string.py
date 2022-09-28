#!/usr/bin/python3
"""function returns the JSON representation of an object (string)
"""
from json import dumps


def to_json_string(my_obj):
    """returns a json

    Args:
        my_obj (str): the string to be jsonified

    Returns:
        str: jsonified str
    """
    return dumps(my_obj)
