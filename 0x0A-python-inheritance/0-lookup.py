#!/usr/bin/python3
"""Lookup into an object"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj (any): any object to be looked up

    Returns:
        list: available attributes and methods
    """
    return dir(obj)
