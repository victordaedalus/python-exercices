"""
Faça uma função que receba dois numeros e retorne qual o maior deles.
author:VictorDaedalus
"""


def bigger(a, b):
    if a > b:
        return a
    elif a == b:
        return False
    else:
        return b


print(bigger(1, 4))
