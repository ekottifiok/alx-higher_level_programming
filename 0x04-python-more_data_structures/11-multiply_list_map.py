#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    new_list = []
    if my_list is not None and len(my_list) > 0:
        for i in my_list:
            new_list.append(i*number)
    return new_list
