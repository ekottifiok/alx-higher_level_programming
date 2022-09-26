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
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: str):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
