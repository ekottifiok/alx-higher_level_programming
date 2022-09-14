#!/usr/bin/python3
"""
Module 2-square
Define class Square
Private instance attribute: size
Instantiation with size (with checks like type and value)
"""


class Square:
    """Generates a square but still building
            builds an instance with a known size
    """

    def __init__(self, size=0):
        """Initializes a private instance attribute

        Args:
                size (any): The size of a square is crucial for a square,
                many things depend of it (area computation, etc.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
