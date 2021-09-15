#!/usr/bin/python3
def search_replace(my_list, search, replace):
        new_list = [None] * len(my_list)
        index = 0
        for i in my_list:
                if i == search:
                        new_list[index] = replace
                else:
                        new_list[index] = my_list[index]
                index += 1
        return new_list
