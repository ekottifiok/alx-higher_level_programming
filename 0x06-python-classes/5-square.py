#!/usr/bin/python3
"""
Module 5-square
Define class Square
Private instance attribute: size
Instantiation with size (with checks like type and value)
Public instance method: def area(self): that returns the current square area
Private instance attribute: (size)
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
Public instance method: def my_print(self): that prints
in stdout the square with the character #:
    if size is equal to 0, print an empty line
    position should be use by using space -
        Dont fill lines by spaces when position[1] > 0
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

    def my_print(self):
        """Prints the square in form of an asterisk
        """
        if not self.__size:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end="")
                print()
