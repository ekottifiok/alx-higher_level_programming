#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    check_list = []
    for i in my_list:
        if i not in check_list:
            check_list.append(i)
            result += i

    return result
