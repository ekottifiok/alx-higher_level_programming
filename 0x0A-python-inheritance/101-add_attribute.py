#!/usr/bin/python3
"""add attributes if it doesn't exist
"""


def add_attribute(obj: any, new_attr: str, value: str):
    """adds a new attribute to an object

    Args:
        obj (any): the object where the new attribute is to be added
        new_attr (str): the title of the new attribute
        value (str): the value to be stored in the attribute

    Raises:
        TypeError: if the object doesn't have the __dict__ holder
        to store attributes example str
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, new_attr, value)
