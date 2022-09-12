#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list == [] or x == 0:
        return
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError,):
            break
        i += 1
    print()
    return i
