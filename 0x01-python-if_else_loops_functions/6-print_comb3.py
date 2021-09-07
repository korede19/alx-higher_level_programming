#!/usr/bin/python3
for i in range(0, 100):
        decena = i / 10
        unidad = i % 10
        if unidad > decena and i < 89:
                print('{:02d}, '.format(i), end='')
        elif i == 89:
                print('{:02d}'.format(i))
