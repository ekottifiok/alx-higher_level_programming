#!/usr/bin/python3
"""
Module 101-square
Define class Square
Private instance attribute: size
Instantiation with size (with checks like type and value)
Public instance method: def area(self): that returns the current square area
Private instance attribute: (size)
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
#:
Public instance method: def my_print(self):
that prints in stdout the square with the character
    if size is equal to 0, print an empty line
    position should be use by using space -
    Dont fill lines by spaces when position[1] > 0
"""


class Square:
    """Generates a square but still building
                    builds an instance with a known size
    """

    def __init__(self, size=0, position=(0, 0)):
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
            self.__position = position
            
    def __str__(self):
        to_print = ''
        if self.__size != 0:
            if self.__position[1] != 0:
                to_print += '\n' * self.__position[1]
            for ch in range(self.__size):
                to_print += ' ' * self.__position[0]
                to_print += '#' * self.__size
                if ch != self.__size - 1:
                    to_print += '\n'
        else:
            to_print = ''
        return to_print

    def area(self):
        """returns the area of the square

        Returns:
                        int: the square of the size
        """
        return self.size ** 2

    @property
    def size(self):
        """returns the size of the square

        Returns:
            int: the size of square
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
            self.size = value

    @property
    def position(self):
        """returns the position of the square

        Returns:
            int: _description_
        """
        return self.position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                isinstance(value[0], int) or isinstance(value[1], int) \
                or (value[0] > 0 and value[1] > 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def my_print(self):
        """Prints the square in form of an asterisk
        """
        
        if self.__size != 0:
            if self.__position[1] != 0:
                    print('\n' * self.__position[1])
            for i in range(self.size):
                
                if self.position[0] > 0:
                    for i in range(self.position[0]):
                        print(" ", end="")
                for j in range(self.size):
                    print('#', end="")
                print()
        else:
            print()
