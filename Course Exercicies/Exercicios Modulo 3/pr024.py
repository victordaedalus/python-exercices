"""
Divisores e soma deles
"""

num = int(input('Digite o numero: '))
soma = 0
for i in range(1, num):
    if (num % i) == 0:
        print('{} é divisor de {}'.format(i, num))
        soma += i

print('A soma de todos os divisores foi de {}'.format(soma))
