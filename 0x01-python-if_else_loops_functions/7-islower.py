#!/usr/bin/python3
def islower(c):
    if c == '':
        raise Exception("Not allowed")
    elif 'a' <= c <= 'z':
        return True
    return False
