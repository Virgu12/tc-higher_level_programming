#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new_value = int(value)
        print("{:d}".format(new_value))
        return True
    except ValueError:
        return False
    


value1 = 89
has_been_print = safe_print_integer(value1)
if not has_been_print:
    print("{} is not an integer".format(value))

value2 = -89
has_been_print = safe_print_integer(value2)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
