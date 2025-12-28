#!/usr/bin/python3
from functools import reduce


def calc_average(a_dictionary):
   average_salary = reduce(lambda x, y: x + y['salary'] / len(a_dictionary), a_dictionary, 0)
   average_age = reduce(lambda x, y: x + y['age'] / len(a_dictionary), a_dictionary, 0)
   return average_salary, average_age
