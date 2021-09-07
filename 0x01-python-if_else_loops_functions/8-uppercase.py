#!/usr/bin/python3
def uppercase(str):
        for i in str:
                char = ord(i)
                if char >= 97 and char <= 122:
                        char -= 32
                print('{:c}'.format(char), end='')
        print()
