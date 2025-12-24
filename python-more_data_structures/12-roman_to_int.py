#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        for s in range(len(roman_string) - 1):
            atual = ROMAN[roman_string[s]]
            seguinte = ROMAN[roman_string[s + 1]]
            if atual < seguinte:
                total -= atual
            else:
                total += atual
        total += ROMAN[roman_string[-1]]
        return total
