#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """Creates an empty Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width > 0 and self.__height > 0:
            return (self.__height * 2) + (self.__width * 2)
        return 0

    def __str__(self) -> str:
        value = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                value += ("#"*self.__width)
                if i < self.__height - 1:
                    value += '\n'
        return value

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
