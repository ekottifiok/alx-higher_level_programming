#!/usr/bin/python3
"""function reads file
"""


def read_file(filename=""):
    """reads a file

    Args:
        filename (str, optional): the file name specified. Defaults to "".
    """
    if filename == "" or not isinstance(filename, str):
        return
    with open(filename, encoding="utf-8") as file_data:
        print(file_data.read(), end="")
