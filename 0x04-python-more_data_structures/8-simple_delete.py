#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None and isinstance(a_dictionary, dict) and a_dictionary.get(key) is not None:
        a_dictionary.pop(key)            
        return a_dictionary
