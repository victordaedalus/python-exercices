"""
Fazer 2 vetores que recebecem 10 numeros cada, e após isso criasse um 3º vetor onde todas as posições pares receberiam
os valores do primeiro vetor, e as posições impares recebessem os valores do segundo vetor.
author:ghostborn67
"""

vetor1 = []  # Posições Pares
vetor2 = []  # Posições Impares
vetor3 = []

print('Vetor 1:')
for i in range(10):
    vetor1.append(int(input(f'Digite o {i + 1}º Numero: ')))

print('Vetor 2:')
for i in range(10):
    vetor2.append(int(input(f'Digite o {i + 1}º Numero: ')))

for i in range(20):
    if (i % 2) == 0:
        vetor3.append(vetor1.pop(0))
    else:
        vetor3.append(vetor2.pop(0))

print(vetor3)
