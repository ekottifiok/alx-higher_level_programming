#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    while(1):
        for i in range(1, 3):
            print(result)
            if i > a:
                result += (i / (a ** b))
            return result
        return result

    return result

