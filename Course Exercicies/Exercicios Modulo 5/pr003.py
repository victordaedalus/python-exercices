"""
Função que verifica um numero, e se for positivo, ele retorna 1, se for negativo ele retorna -1, se for 0 ele retorna 0.
author:victordaedalus
"""


def tipo(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0


num = int(input('Digite um numero: '))
print(tipo(num))
