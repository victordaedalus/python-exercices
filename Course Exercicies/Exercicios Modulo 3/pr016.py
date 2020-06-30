"""
Contador de Numeros Pares de Impares em ordem decrecente
author: ghostborn67
"""

num = int(input('Digite Um Numero Inteiro: '))
if (num % 2) == 0:
    for i in range(num - 1, 0, -2):
        print(i)
else:
    for i in range(num, 0, -2):
        print(i)
