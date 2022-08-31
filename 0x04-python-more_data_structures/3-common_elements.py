#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_ret = []
    if (len(set_1) > 0 and len(set_2) > 0):
        for i in set_1:
            for j in set_2:
                if i == j:
                    set_ret.append(i)
    return set_ret
