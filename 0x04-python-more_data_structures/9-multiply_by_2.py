#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        for key in a_dictionary.keys():
            a_dictionary[key] = a_dictionary.get(key) * 2
    return a_dictionary
