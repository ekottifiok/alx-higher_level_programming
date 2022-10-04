#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    if filename == "" or search_string == "" or new_string == "":
        return
    with open(filename, 'r+') as file:
        x = file.read()
        file.seek(0)  
        file.truncate()
        file.write(x.replace(search_string, new_string))
