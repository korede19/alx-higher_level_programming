#!/usr/bin/python3
def print_last_digit(number):
        value = number % 10
        if number < 0:
                value = (number * -1) % 10
        print(value, end='')
        return value
