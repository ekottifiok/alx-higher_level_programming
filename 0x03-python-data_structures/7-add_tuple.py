#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    answer = []
    for i in range(2):
        try:
            j = list_a[i]
        except IndexError:
            j = 0
        try:
            k = list_b[i]
        except IndexError:
            k = 0
        answer.append(j + k)
    return (tuple(answer))
