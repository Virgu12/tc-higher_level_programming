#!/usr/bin/python3
from functools import reduce


def calc_average(a_dictionary):
    if not isinstance(a_dictionary, list):
        return 0, 0
   
    total_salary = reduce(lambda x, y: x + y['salary'], a_dictionary.values(), 0)
    total_age = reduce(lambda x, y: x + y['age'], a_dictionary.values(), 0)
    average_salary = total_salary / len(a_dictionary)
    average_age = total_age / len(a_dictionary)
    return average_salary, average_age
