#!/usr/bin/python3
"""
Module Magic class

Raises:
    TypeError: ensures the type is int or float

Returns:
    int: the area and circumference
"""
import math


class MagicClass:
    """the magic class
    """

    def __init__(self, radius):
        """initializes an instance of the class

        Args:
            radius (int): the radius of the circle

        Raises:
            TypeError: ensures the radius is either an int or float
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """computes the area of the circle

        Returns:
            int: the area
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """circumference computed

        Returns:
            int: the computed circumference
        """
        return 2 * math.pi * self._MagicClass__radius
