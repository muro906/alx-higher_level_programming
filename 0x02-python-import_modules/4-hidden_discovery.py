#!/usr/bin/python3
if __name__ == "__main__":
    module = dir(hidden_4.pyc)
    for arg in module:
        if arg[0] == '_':
            continue
        print(arg)
