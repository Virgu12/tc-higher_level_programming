#!/usr/bin/python3
def safe_print_division(a, b):
    try:
         conta = a / b
         return conta
    except ZeroDivisionError:
        conta = None
        return conta 
    finally:
        print('Inside result:' "{}".format(conta))