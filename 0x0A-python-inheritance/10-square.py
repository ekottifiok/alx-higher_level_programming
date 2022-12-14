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
        """initializes the class

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
