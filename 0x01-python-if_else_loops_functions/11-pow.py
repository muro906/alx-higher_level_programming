#!/usr/bin/python3
def pow(a, b):
    base = a
    if b > 0:
        for i in range(1, b):
            a = a * base
        return a
    elif b == 0:
        return 1
    else:
        for i in range(b, -1):
            a = a * base
        return 1 / a
