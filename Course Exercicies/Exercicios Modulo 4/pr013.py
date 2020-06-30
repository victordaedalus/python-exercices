"""
Vetor recebe 5 valores e mostra a posição do menor e maior valor, além de mostra-los.
author:ghostborn67
"""

# Var
vetor = []

# Run
for i in range(5):
    vetor.append(int(input(f'{i + 1}° $> ')))

maior = max(vetor)
menor = min(vetor)

print(f'O Maior Numero está na posição {vetor.index(maior)}, '
      f'e o Menor Numero está na posição {vetor.index(menor)}.')
