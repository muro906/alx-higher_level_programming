#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    module = dir(hidden_4)
    for arg in module:
        if arg[:2] == '__':
            continue
        print(arg)
