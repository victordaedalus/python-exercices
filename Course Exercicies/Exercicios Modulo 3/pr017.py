"""
Calculador de  Numeros Naturais
author: ghostborn67
"""
n = int(input('Digite um Numero Inteiro: '))
counter = 1
media = 0
for i in range(n):
    media += counter
    counter += 1
print(media)
