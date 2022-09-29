#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """handles the main idea behind the pascal triangle

    Args:
        n (int): size of the triangle

    Returns:
        array: the pascal triangle
    """
    if not isinstance(n, int):
        return []
    list_re = []
    for i in range(n):
        value = [1]
        if i == 0:
            list_re.append(value)
        else:
            if i > 1:
                for j in range(1, i):
                    value.append(list_re[-1][j] + list_re[-1][j-1])
            list_re.append(value+[1])
    return list_re
