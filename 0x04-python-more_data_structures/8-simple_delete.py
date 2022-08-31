#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if isinstance(a_dictionary, dict):
        a_dictionary.pop(key)
    return a_dictionary
