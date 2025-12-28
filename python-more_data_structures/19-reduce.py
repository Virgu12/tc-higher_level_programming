#!/usr/bin/python3
from functools import reduce


def calc_average(a_dictionary):   
    if not isinstance(a_dictionary, list):
        return 0,0

    salaries = map(lambda p: p['salary'], a_dictionary)
    ages = map(lambda p: p['age'], a_dictionary)

    total_salary = reduce(lambda total, salarios: total + salarios, salaries, 0)
    total_age = reduce(lambda total, idades: total + idades, ages, 0)
    
    average_salary = total_salary / len(a_dictionary)
    average_age = total_age / len(a_dictionary)
    return average_salary, average_age
