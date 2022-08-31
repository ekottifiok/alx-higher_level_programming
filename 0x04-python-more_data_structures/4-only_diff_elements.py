#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_ret = []
    diff_ret = []
    if (len(set_1) > 0 and len(set_2) > 0):
        for i in set_1:
            for j in set_2:
                if i == j:
                    set_ret.append(i)
        for i in set_1:
            if i not in set_ret and i not in diff_ret:
                diff_ret.append(i)
        for j in set_2:
            if j not in set_ret and j not in diff_ret:
                diff_ret.append(j)
    return diff_ret
