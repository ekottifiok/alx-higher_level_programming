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

    def __init__(self, x) -> None:
        if isinstance(x, int):
            self.__x = x

    def __eq__(self, __y: object) -> bool:
        return self.__x != __y

    def __ne__(self, __y: object) -> bool:
        return self.__x == __y
