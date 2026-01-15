#!/usr/bin/python3
"""
Module provides a function print the first and last name
Includes type checking

"""


def say_my_name(first_name, last_name=""):
    """
    receive two string:
    args:
    first_name = a string
    last_name = a string

    return:
        the string return the "My name is <first name> <last name>"
    
    raise:
        TypeError: if not a string
    """
    name_errorF = "first_name must be a string"
    name_errorL = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(name_errorF)
    if not isinstance(last_name, str):
        raise TypeError(name_errorL)
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
