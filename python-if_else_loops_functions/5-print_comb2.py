#!/usr/bin/python3
for number in range(0, 100):
   f = f"{number:02}" if number < 10 else str(number)
   print("{}" .format(f), end=', ' if number != 99 else '\n')
