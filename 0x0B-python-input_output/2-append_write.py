#!/usr/bin/python3
"""function appends to file
"""


def append_write(filename="", text=""):
    """appends to a file

    Args:
        filename (str, optional): the file name specified. Defaults to "".
        text (str, optional): the text to be written. Defaults to "".

    Returns:
        int: the number of characters written
    """
    if filename == "" or text == "" or not isinstance(filename, str):
        return
    with open(filename, "a", encoding="utf-8") as file_data:
        return file_data.write(text)
