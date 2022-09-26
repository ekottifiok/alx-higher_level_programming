#!/usr/bin/python3
"""the square class for instantiation

Returns:
    str: from the str
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """generates a instance of a square

    Args:
        Rectangle (class): the rectangle class
    """

    def __init__(self, size: int):
        super().__init__(size, size)
