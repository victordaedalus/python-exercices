"""
Ler um vetor de 10 números, e mostrar quantos números pares o mesmo possui.
author:ghostborn67
"""
def par(x):
    if (x % 2) == 0:
        return True
    else:
        return False

# Variables
vetor = []
pares = 0

# Execution
for i in range(10):
    vetor.append(int(input(f'Digite o {i + 1} número: ')))

for valor in vetor:
    if par(valor):
        pares += 1

print(f'O vetor possui {pares} números pares.')
