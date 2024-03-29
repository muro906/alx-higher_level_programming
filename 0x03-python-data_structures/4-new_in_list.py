#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) == 0 or idx >= len(my_list) or idx < 0:
        return my_list.copy()
    new = my_list.copy()
    new.pop(idx)
    new.insert(idx, element)
    return new
