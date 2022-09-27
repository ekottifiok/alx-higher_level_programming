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
    # def __str__(self):
    #     """handles the print of the class

    #     Returns:
    #         str: returns a list of the class
    #     """
    #     return str(list(i for i in self))

    def print_sorted(self):
        """prints a sorted version of the list
        """
        print(sorted(self))
