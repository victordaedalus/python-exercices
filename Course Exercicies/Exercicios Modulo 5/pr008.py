"""
Fazer uma função que receba os catetos "a" e "b" e calcule a hipotenusa pela equação abaixo:

hip = sqrt(a² + b²)

author:VictorDaedalus
"""
from math import sqrt


def hypotenuse(a=1, b=2):
    hip = sqrt(a ** 2 + b ** 2)
    return hip


print(hypotenuse(15, 20))
