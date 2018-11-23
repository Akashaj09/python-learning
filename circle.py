# circle area
from math import pi


def circle_area(r):
    if r < 0 :
        raise ValueError("Number can't be negative")
    if type(r) not in [int, float]:
        raise TypeError("Number must be float or integer")
    return pi * (r ** 2)
