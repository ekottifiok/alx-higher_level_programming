#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    try:
        a_dictionary[key] = value
    except Exception:
        print("sorry")
    return a_dictionary
