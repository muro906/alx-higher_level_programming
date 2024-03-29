#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    for x in my_list:
        print("{:d}".format(x))
