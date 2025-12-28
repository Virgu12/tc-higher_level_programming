#!/usr/bin/python3
def filtering_data(a_dictionary):
    filtro = list(filter(lambda emp: emp['salary'] > 10000, a_dictionary))
    nomes = list(map(lambda emp: emp['name'], filtro))
    return nomes
