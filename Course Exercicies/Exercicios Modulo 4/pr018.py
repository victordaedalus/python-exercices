"""
Fazer uma lista que leia 10 numeros, leia um numero X, 
e após fale quais numeros da listas são multiplos de X.
author:ghostborn67
"""

vetor = []

for i in range(10):
    vetor.append(int(input(f'Digite o {i + 1} Numero: ')))

x = int(input('Digite o X: '))

for i in vetor:
    if i < x:
        pass
    else:
        if i % x == 0:
            print(i)
