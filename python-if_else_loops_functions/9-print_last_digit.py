#!/usr/bin/python3
def print_last_digit(number):
    ul = abs(number) % 10
    print(ul, end="")
    return ul
