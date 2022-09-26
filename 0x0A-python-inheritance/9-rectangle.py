#!/usr/bin/python3
"""the rectangle class for instantiaion

Returns:
    str: from the str
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """generates an object with basegeometry

    Args:
        BaseGeometry (class): has some validators and checks
    """

    def __init__(self, width: int, height: int):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
