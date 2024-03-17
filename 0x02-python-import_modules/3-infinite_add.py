#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    if len(sys.argv) == 1:
        print(add)
        sys.exit()
    else:
        for i in sys.argv[1:]:
            add += int(i)
        print(add)
