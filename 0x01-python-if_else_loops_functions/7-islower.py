#!/usr/bin/python3
def islower(c):
    if c == '"' or '\'\'':
        raise TypeError
        return
    elif c >= 'a' and c <= 'z':
        return True
    return False
