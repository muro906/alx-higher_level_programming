#!/usr/bin/python3
def islower(c):
    if c == '"':
        raise TypeError
    elif c >= 'a' and c <= 'z':
        return True
    return False
