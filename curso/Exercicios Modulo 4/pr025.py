"""
Fazer um programa que preencha um vetor de 100 indices com os primeiros
100 numeros naturais que não são multiplos de 7 ou que terminam com 7.
author:ghostborn67
"""

numeros = []
contador = 0

while True:
    if len(numeros) <= 100:
        contador += 1
        if not contador % 7 == 0 or str(contador)[-1] == '7':
            numeros.append(contador)
    else:
        break

print(numeros)
