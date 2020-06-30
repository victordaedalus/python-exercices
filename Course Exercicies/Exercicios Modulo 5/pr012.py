"""
Fazer uma função que receba um numero inteiro e maior que zero, e calcule todos os seus algorismos.

Ex: (1240) = 1 + 2 + 4 + 0 == 7

author:VictorDaedalus
"""


def algorism_calc(numero):
    alg_sum = 0
    if type(numero) is int and numero > 0:
        for alg in str(numero):
            alg_sum += int(alg)
        return alg_sum
    else:
        print('Numero Inválido...')


print(algorism_calc(1240))
