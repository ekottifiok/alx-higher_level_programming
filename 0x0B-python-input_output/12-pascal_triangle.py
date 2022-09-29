#!/usr/bin/python3
def pascal_triangle(n):
    list_re = []
    for i in range(n):
        value = [1]
        if i == 0:
            list_re.append(value)
        elif i == 1:
            list_re.append(value+[1])
        else:
            for j in range(1,i):
                value.append(list_re[-1][j] + list_re[-1][j-1])
            list_re.append(value+[1])
    return list_re