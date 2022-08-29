#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for i in range(len(tuple_b)):
        list_a[i] += list_b[i]
    return (tuple(list_a))
