#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for nm in my_list:
        new_list.append(nm % 2 == 0)
    return new_list
abe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 40]
print(divisible_by_2(abe))

    