"""
Criar Dois Vetores 'A' e 'B' que receberam 10 numeros cada, e calcular um vetor 'C' que recebera:
C = A - B

author:ghostborn67
"""

vetorA = []
vetorB = []
vetorC = []

print('Adicionando Números ao Vetor A')
for num in range(1, 11):
    vetorA.append(int(input(f'Digite o {num}º do vetor: ')))

print('Adicionando Números ao Vetor B')
for num in range(1, 11):
    vetorB.append(int(input(f'Digite o {num}º do vetor: ')))

for x in range(10):
    vetorC.append(int(vetorA[x] - vetorB[x]))

print(vetorC)