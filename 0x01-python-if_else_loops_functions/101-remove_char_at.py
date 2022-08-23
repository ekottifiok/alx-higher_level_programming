#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    buffer = ''
    for c in str:
        if i != n:
            buffer += c
        i += 1
    return buffer
