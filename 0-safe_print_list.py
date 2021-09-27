#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        j = 0
        try:
                for i in my_list:
                        if j == x:
                                break
                        print("{:d}".format(i), end="")
                        j += 1
        except IndexError:
                print("Index out range")
        finally:
                print()
        return (j)
