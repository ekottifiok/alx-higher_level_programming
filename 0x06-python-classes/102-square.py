#!/usr/bin/python3
"""
Module 102-square
Define class Square
Private instance attribute: size
Instantiation with size (with checks like type and value)
Public instance method: def area(self): that returns the current square area
Private instance attribute: (size)
property def size(self): to retrieve it
property setter def size(self, value): to set it
comparing with other similar Square instance is possible
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __str__(self):
        return str(self.__size)

    def area(self):
        """returns the area of the square

        Returns:
                area: the square of the size
        """
        return self.__size ** 2

    @property
    def size(self):
        """returns the size of the square

        Returns:
                size: the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that returns to the current the square area of the object

        Args:
            value (int): the value to set the size

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __le__(self, other):
        """True if self is less or equal than other"""
        return self.area() <= other.area()

    def __lt__(self, other):
        """True if self is less than other"""
        return self.area() < other.area()

    def __eq__(self, other):
        """True if self is equal than other"""
        return self.area() == other.area()

    def __ge__(self, other):
        """True if self is greater or equal than other"""
        return self.area() >= other.area()

    def __gt__(self, other):
        """True if self is greater than other"""
        return self.area() > other.area()

    def __ne__(self, other):
        """True if self is not equeal other"""
        return self.area() != other.area()
