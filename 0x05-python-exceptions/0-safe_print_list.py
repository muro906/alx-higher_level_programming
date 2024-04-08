#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            print(i, end='')
            count += 1
        print()
    except IndexError:
        pass
    else:
        return count
