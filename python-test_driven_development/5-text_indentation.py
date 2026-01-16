#!/usr/bin/python3
"""
Module provides a function that
prints a text with 2 new lines after each of these characters: ., ? and :
Includes type checking
"""


def text_indentation(text):
    """
    arg:
    text = a str

    return:
        text with 2 new lines after each of these characters: ., ? and :

    raise:
        TypeError: if not string

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    punctuation = [".", "?", ":"]
    tex = text.strip()

    new_line = False
    for letter in tex:
        if new_line and letter == " ":
            continue

        new_line = False

        if letter in punctuation:
            print(letter, end="\n")
            print()
            new_line = True
        else:
            print(letter, end="")
