#!/usr/bin/python3
"""making some inverted operations with equals to and not equals

Returns:
    int: the resulting inverted operation
"""


class MyInt(int):
    """Inherits from the int class

    Args:
        int (class): main class that we inherit from
    """

    def __init__(self, x):
        """initializes the class

        Args:
            x (int): setups a class
        """
        if isinstance(x, int):
            self.__x = x

    def __eq__(self, __y: object):
        """returns true if equal to self

        Args:
            __y (object): the object to be compared

        Returns:
            bool: true if equals
        """
        return self.__x != __y

    def __ne__(self, __y: object):
        """if not equal to

        Args:
            __y (object): the object to be compared

        Returns:
            bool: true if not equals
        """
        return self.__x == __y
