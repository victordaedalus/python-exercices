"""
Criar um vetor que receba 15 numeros, e depois disso compacta-lo, ao remover todos os numeros 0 do vetor. 
author:ghostborn67
"""

vetor = []

for i in range(1, 16):
    vetor.append(int(input(f'Digite o {i}° numero do vetor: ')))

for num in vetor:
    if num == 0:
        vetor.pop(vetor.index(num))

print(vetor)
