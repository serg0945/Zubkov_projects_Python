from math import pi

default_radius = 5

def circle_perimeter(radius=default_radius):
    return 2 * pi * radius

def circle_area(radius=default_radius):
    return pi * (radius ** 2)

