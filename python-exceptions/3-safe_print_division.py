#!/usr/bin/python3
def safe_print_division(a, b):
    conta = None
    try:
         conta = a / b
    except ZeroDivisionError:
        conta = None
    finally:
        print('Inside result:' "{}".format(conta))
        return conta
