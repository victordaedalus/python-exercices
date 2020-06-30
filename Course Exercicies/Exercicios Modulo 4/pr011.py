"""
Criar um vetor que receba 10 numeros reais, e calcular a quantidade de numeros negativos e
apresentar a soma de todos os numeros positivos.
author:ghostborn67
"""

# Var
vetor = []
neg = 0
posi = 0

# Run
for i in range(10):
    vetor.append(float(input(f'Digite {i +1}° número: ')))

for x in vetor:
    if x < 0:
        neg += 1
    else:
        posi += x

print(f'O vetor possui {neg} numeros negativos, e a soma dos positivos igual a {posi}.')
