#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        add = 0
        for arg in argv[1:]:
            add += int(arg)
        print(add)
