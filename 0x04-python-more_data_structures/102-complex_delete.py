#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        key_list = list(a_dictionary.keys())[:]
        for key in key_list:
            if a_dictionary.get(key) == value:
                a_dictionary.pop(key)
        return a_dictionary
