#!/usr/bin/python3
def zipping_data(list1,list2):
    for list1, list2 in zip(list1, list2):
        print(f"{list1}: R$ {list2:.2f}")
