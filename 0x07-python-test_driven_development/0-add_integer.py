"""Adds two numbers and makes sure they are of type int or float
"""


def add_integer(a, b=98):
    """adds two numbers together

    Args:
        a (int): number 1
        b (int, optional): number 2. Defaults to 98.

    Raises:
        TypeError: a and b must be int or floats

    Returns:
        int: sum of the two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    print(int(a + b))
