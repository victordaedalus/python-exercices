"""
Fazer função que recebe altura e raio de um cilindro e retorne o volume.
A equação é:

V = pi * r² * h

author:VictorDaedalus
"""
from math import pi


def cylinder_vol(r, h):
    vol = pi * r ** 2 * h
    return vol


print(cylinder_vol(30, 100))
