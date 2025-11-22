#!/usr/bin/python3
for primeiro in range(0, 10):
    for segundo in range(primeiro + 1, 10):
        print("{}{}".format(primeiro, segundo), end=", " if int("{}{}".format(primeiro, segundo)) != 89 else "\n")