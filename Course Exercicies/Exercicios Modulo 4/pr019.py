"""
Criar um vetor de 50 posições que cumpra as regras determinadas de equação seguintes:

(i + 5 * i)%(i + 1)

Em seguida imprimir vetor na tela.

author:ghostborn67
"""

vetor = []

for i in range(1, 51):
    vetor.append((i + 5 * i)%(i + 1))

print(vetor)
