"""
Contador de Divisores
"""

num = int(input('Digite o Numero: '))
for i in range(1, num + 1):
    if (num % i) == 0:
        print('{} é divisor de {}'.format(i, num))
