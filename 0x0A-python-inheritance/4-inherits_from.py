#!/usr/bin/python3
"""checks if the class is inherited another class"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False

    Args:
        obj (any): object to check
        a_class (any): the class

    Returns:
        bool: True if type of obj eq a_class
    """
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    return False
