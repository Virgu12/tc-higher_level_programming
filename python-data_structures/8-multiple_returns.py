#!/usr/bin/python3
def multiple_returns(frase=None):
    length = len(frase)
    first = frase[0] if frase else None
    return (length, first)
