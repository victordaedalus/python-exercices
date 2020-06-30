"""
Criar um vetor que receberá 6 números e imprimir o mesmo inversamente.
author:ghostborn67
"""
lista = []

for i in range(6):
    lista.append(int(input(f'Digite o {i + 1}° numero: ')))

lista.reverse()
print(lista)
