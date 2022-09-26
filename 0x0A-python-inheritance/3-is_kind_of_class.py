#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of,
    or if the object is an instance
    of a class that inherited from, the specified class ; otherwise False.

    Args:
        obj (any): object to check
        a_class (any): the class

    Returns:
        bool: True if type of obj eq a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
