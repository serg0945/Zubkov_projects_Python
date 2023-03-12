from math import sqrt

default_a = 7
default_b = 2
default_c = 8

def triangle_perimetr(a=default_a, b=default_b, c=default_c):
    return a + b + c

def triangle_area(a=default_a, b=default_b, c=default_c):
    p = (a + b + c) / 2
    return sqrt(p * (p-a) * (p-b) * (p-c))

