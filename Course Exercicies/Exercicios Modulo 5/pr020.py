"""
Fazer uma funcao que calcule o fatorial do numero (n) e mostre na tela.

author:VictorDaedalus
"""


def factorial(n):
    counter = 1
    while counter >= n:
        n *= counter
        counter += 1
        print(n)
    return n


print(factorial(3))
