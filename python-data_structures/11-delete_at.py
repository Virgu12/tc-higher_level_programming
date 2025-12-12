#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if  idx < 0 or idx >= len(my_list):
        return my_list
    for nm in range(len(my_list)):
        if idx != nm:
            new_list.append(my_list[nm])
    return new_list
