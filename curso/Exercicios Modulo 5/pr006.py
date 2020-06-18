"""
Fazer uma função que receba 3 paramentros, sendo esses: horas, minutos e segundos.
Em seguida converter todos os parametros para segundos.
author:VictorDaedalus  
"""


def crono_convert(h=0, m=0, s=0):
    m += h * 60
    s += m * 60
    return s


print(f'{crono_convert(1, 30)} segundos.')
