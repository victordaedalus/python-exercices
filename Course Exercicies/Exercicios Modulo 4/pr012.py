"""
Vetor com 5 valores,
Mostrar todos os valores, o maior e o menor, além de mostrar a media
author:ghostborn67
"""

# Var
vetor = []

# Run
for i in range(5):
    vetor. append(int(input(f'Digite o {i + 1}° Número: ')))

maior = max(vetor)
menor = min(vetor)

media = sum(vetor) / 5
print(f"""
O vetor é {vetor},
Seu Maior Número é {maior},
Seu Menor Número é {menor},
A Média Numérica do vetor é de ({media}).""")
