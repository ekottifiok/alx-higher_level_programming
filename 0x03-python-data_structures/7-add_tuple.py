#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(len(tuple_a)):
        new_tuple[i] = tuple_a[i] + tuple_b[i]