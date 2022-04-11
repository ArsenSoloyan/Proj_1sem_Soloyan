from math import pi

default_radius = 5
__all__ = ['circle_perimeter', 'circle_area']

def circle_perimeter(r=default_radius):
    return pi * 2 *r

def circle_area(r=default_radius):
    return pi * r ** 2
