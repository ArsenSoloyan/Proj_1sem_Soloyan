import math
from math import sqrt
a,b,c = 7,2,8
__all__ = ['triangle_perimeter', 'triangle_area']

def triangle_perimeter(a_a=a,b_b=b,c_c=c):
    return a_a + b_b + c_c

def triangle_area(a_a=a,b_b=b,c_c=c):
    return math.sqrt(((a_a + b_b + c_c) / 2) * (((a_a + b_b + c_c) / 2) - a_a) * (((a_a + b_b + c_c) / 2) - b_b) * (((a_a + b_b + c_c) / 2) - c_c))
