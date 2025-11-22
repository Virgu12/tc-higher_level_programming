#!/usr/bin/python3
for primeiro in range(0, 10):
    for segundo in range(primeiro + 1, 10):
        numero = "{}{}".format(primeiro, segundo)
        print(numero, end=", " if int(numero) != 89 else "\n")
