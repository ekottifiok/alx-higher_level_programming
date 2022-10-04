#!/usr/bin/python3
"""append after"""

def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    if filename == "" or search_string == "" or new_string == "":
        return
    with open(filename, 'r+') as file:
        x = file.read()
        file.seek(0)  
        file.truncate()
        file.write(x.replace(search_string, new_string))
