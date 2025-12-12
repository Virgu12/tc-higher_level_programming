#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    apd = (tuple_a + (0, 0))[:2]
    bpd = (tuple_b + (0, 0))[:2]
    soma = tuple(x + y for x, y in zip(apd, bpd))
    return soma
