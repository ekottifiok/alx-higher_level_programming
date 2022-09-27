#!/usr/bin/python3
"""BaseGeometry Module

Raises:
    Exception: returns a joke
    TypeError: checks for int
    ValueError: check that the number is > 0
"""


class BaseGeometry:
    """generates an instance for base geometry
    """

    def area(self):
        """returns a joke not implemented

        Raises:
            Exception: joke
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        """validates an input integer

        Args:
            name (str): the name of the input
            value (int): the value of the input

        Raises:
            TypeError: raises when not integer
            ValueError: if not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
