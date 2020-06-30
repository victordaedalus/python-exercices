"""
Digitar um vetor com 10 valores e ao final mostrar qual foi o maior e o menor valor.
author:ghostborn67
"""

# Variables
vetor = []

# Execution

for i in range(10):
    vetor.append(int(input(f'Digite o {i + 1}° valor: ')))

maior = max(vetor)
menor = min(vetor)

print(f'O Maior Número foi {maior}, e o Menor foi {menor}.')
