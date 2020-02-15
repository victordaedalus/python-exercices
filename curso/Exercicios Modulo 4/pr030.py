"""
Criar dois vetores que leia 10 numeros e calcular a intersecção entre eles.
author:ghostborn67

## Modo com a lista...

vetor1 = []
vetor2 = []
inter = []

for x in range(10):
    vetor1.append(int(input(f'Digite o {x + 1}° número do vetor1: ')))

for x in range(10):
    vetor2.append(int(input(f'Digite o {x + 1}° número do vetor2: ')))

for i in vetor1:
    if i in vetor2:
        if i in inter:
            pass
        else:
            inter.append(i)

print('A intersecção dos vetores é de:')
print(inter)
"""

# Usando Conjuntos

vetor1 = set()
vetor2 = set()
inter = set()

for x in range(10):
    vetor1.add(int(input(f'Digite o {x + 1}° número do vetor1: ')))

for x in range(10):
    vetor2.add(int(input(f'Digite o {x + 1}° número do vetor2: ')))

inter = vetor1.intersection(vetor2)

print('A intersecção dos vetores é de:')
print(inter)
