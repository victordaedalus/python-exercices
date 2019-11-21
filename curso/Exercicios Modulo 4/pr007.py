"""
Criar um vetor com 10 numeros e escrever qual o maior, e qual é a sua posição.
author:ghostborn67
"""

# Variables
vetor = []

# Execution=
for x in range(10):
    vetor.append(int(input(f'Digite o {x + 1}° número: ')))

num = max(vetor)
print(f"O maior número foi {num}, na posição {vetor.index(num)}.")
