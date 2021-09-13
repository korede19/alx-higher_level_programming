#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        copy_a = tuple_a + (0, 0)
        copy_b = tuple_b + (0, 0)
        t = copy_a[0] + copy_b[0], copy_a[1] + copy_b[1],
        return t
