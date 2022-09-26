#!/usr/bin/python3
"""inherits from list

Returns:
    list: returns a list
"""


class MyList(list):
    """simple implementation of the list type

    Args:
        list (list): builtin class
    """
    def __str__(self):
        return str(list(i for i in self))

    def print_sorted(self):
        print(sorted(list(i for i in self)))
