"""
Criar um lista que receba 10 numeros e que mostre quais deles são numeros primos e as posições.
author:ghostborn67
"""


def multiplo(numero, mult):
    if numero % mult == 0:
        return True
    else:
        return False


lista = []
primos = []

for i in range(1, 11):
    lista.append(int(input(f'Digite o {i}° Numero: ')))

for local, numero in enumerate(lista):
    if numero == 2 or numero == 3 or numero == 5:
        primos.append([numero, local])
    elif multiplo(numero, 2) is False:
        if multiplo(numero, 3) is False:
            if multiplo(numero, 5) is False:
                primos.append([numero, local])

for i in primos:
    print(f'O numero {i[0]} é primo e ele se encontra no indice {i[1]}')
