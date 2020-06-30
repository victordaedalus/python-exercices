"""
Criar dois vetores que recebam 10 numeros e mostrar a união entre eles
author:ghostborn67
"""

vetor1 = set()
vetor2 = set()

for i in range(10):
    vetor1.add(int(input(f'Digite o {i + 1}° número do vetor1: ')))

for i in range(10):
    vetor2.add(int(input(f'Digite o {i + 1}° número do vetor2: ')))

print('A União entre o vetor 1 e 2 é de:')
print(vetor1.union(vetor2))
