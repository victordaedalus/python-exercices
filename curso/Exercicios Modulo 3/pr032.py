"""
Programa de Lançamento de dados
author:ghostborn67
"""

# Import
import random
from time import sleep

while True:

    print('Lançado dados...')
    sleep(2)

    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)

    print("""
    Valor do Dado1: {}
    Valor do Dado2: {}
    """.format(dado1, dado2))

    if dado1 > dado2:
        print('Dado1 é maior que Dado2')
    elif dado2 > dado1:
        print('Dado2 é maior que Dado1')
    else:
        print('Os dois dados possuem o mesmo valor.')

    sleep(7)

    print(50 * '\n', 'Deseja jogar os dados denovo?')
    print('Digite 1 para Sim ou 2 para não. ')
    counter = int(input('&> '))

    if counter == 1:
        print(70 * '\n')
        print('Reiniciando programa...')
        sleep(4)
        print(70 * '\n')
    else:
        print('Desligando programa....')
        sleep(1)
        break
