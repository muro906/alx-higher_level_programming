#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            val = ord(i) - 32
            print("{}".format(chr(val)), end='')
        else:
            print("{}".format(i), end='')
    print("\n", end='')
