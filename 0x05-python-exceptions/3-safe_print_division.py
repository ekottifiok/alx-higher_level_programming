#!/usr/bin/python3

def safe_print_division(a, b):
    print("Inside result: ", end='')
    try:
        c = str(a/b)

    except (ZeroDivisionError,):
        c = "None"

    print(c)
    return c
