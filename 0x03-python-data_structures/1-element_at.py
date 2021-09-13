#!/usr/bin/python3
def element_at(my_list, idx):
        index = 0
        lenght = len(my_list)
        if idx > lenght or idx < 0:
                return None

        for index in range(lenght):
                if index == idx:
                        return my_list[idx]
                index += 1
