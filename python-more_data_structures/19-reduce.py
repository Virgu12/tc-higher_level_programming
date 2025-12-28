#!/usr/bin/python3
from functools import reduce


def calc_average(a_dictionary):
   average_salary = reduce(lambda x, y: x + y[1]['salary'], a_dictionary.items(), 0) / len(a_dictionary)
   average_age = reduce(lambda x, y: x + y[1]['age'], a_dictionary.items(), 0) / len(a_dictionary)
   return average_salary, average_age
