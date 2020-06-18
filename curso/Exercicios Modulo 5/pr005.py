"""
Fazer um programa que calcula o volume de uma esfera pela equação:

V = 4/3 * pi * r³

author:VictorDaedalus
"""
pi = 3.14


def sphere_volume_calc(radius):
    volume = (4 * pi * (radius ** 3)) / 3
    return volume


print(sphere_volume_calc(float(input("Input the Radius:\n#> "))))
