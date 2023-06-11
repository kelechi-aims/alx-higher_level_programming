#!/usr/bin/python3
def magic_calculation(a, b):
#    from magic_calculation_10 import add, sub
    add = __import__('magic_calculation_02', globals(), locals(), ['add'], 0).add
    sub = __import__('magic_calculation_02', globals(), locals(), ['sub'], 0).sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
