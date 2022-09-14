#!/usr/bin/python3
"""
Module 1-square
Define class Square
Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """Generates a square but still building
            builds an instance with a known size
    """

    def __init__(self, size):
        """Initializes a private instance attribute

        Args:
                size (any): The size of a square is crucial for a square,
                many things depend of it (area computation, etc.
        """
        self.__size = size
