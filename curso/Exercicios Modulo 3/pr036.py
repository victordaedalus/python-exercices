"""
Diferença entre:

Os 100 primeiros numeros quadrado naturais

e

Quadrado da soma dos 100 primeiros numeros naturais
"""

natural_qua = 0
soma_qua = 0

for i in range(1, 101):
    natural_qua += i ** 2
print(f'A soma dos quadrados foi de {natural_qua}')

for i in range(1, 101):
    soma_qua += i
print(f'O quadrado da soma foi de {soma_qua}')

soma_qua = soma_qua ** 2

if natural_qua > soma_qua:
    print(f'Diferença de {natural_qua - soma_qua}')
else:
    print(f'Diferença de {soma_qua - natural_qua}')
