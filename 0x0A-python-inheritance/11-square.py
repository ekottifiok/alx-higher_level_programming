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
        """initializes the class instance

        Args:
            size (int): size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """handles the print call on the instance

        Returns:
            str: custom string to printed out
        """
        return f"[Square] {self.__size}/{self.__size}"
