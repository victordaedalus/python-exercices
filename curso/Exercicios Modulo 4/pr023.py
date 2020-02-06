"""
Receber o valor de duas listas com cada recebendo 5 numeros, e calcular o valor escalar entre os dois,
ao final mostrar na tela as listas e o valor escalar entre elas.
author:ghostborn67
"""

vetorA = []
vetorB = []
escalar = 0

print('Vetor A:')
for i in range(5):
    vetorA.append(float(input(f'Digite o {i + 1}º valor:')))

print('Vetor B:')
for i in range(5):
    vetorB.append(float(input(f'Digite o {i + 1}º valor:')))

for objeto in range(5):
    escalar += vetorA[objeto] * vetorB[objeto]

print(vetorA)
print(vetorB)
print(f'O valor escalar é {escalar}.')
