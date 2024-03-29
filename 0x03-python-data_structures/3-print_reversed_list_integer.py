#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    try:
        if len(my_list) == 0:
            return
        elif len(my_list) > 0:
            my_list.reverse()
            for i in my_list:
                print("{:d}".format(i))
    except TypeError:
        pass
