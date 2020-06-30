"""
Fazer um vetor que receba 10 valores,
e que cada elemento que estiver com o valor negativo receba 0.
author:ghostborn67
"""

lista = []

for i in range(10):
    lista.append(int(input(f'Digite o {i + 1}° elemento: ')))

for x in lista:
    if x < 0:
        lista[lista.index(x)] = 0

print(lista)
