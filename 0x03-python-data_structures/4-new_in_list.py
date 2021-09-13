#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if idx > (len(my_list) - 1) or idx < 0:
                return my_list
        my_copy = my_list.copy()
        my_copy[idx] = element
        return my_copy
