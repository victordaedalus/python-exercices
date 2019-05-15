import math

print('Digite um numero:')
num = float(input())
if num > 0:
    print('O numero ao quadrado é igual á {}'.format(num ** 2))
    print('E a raiz quadrada do mesmo é igual á {}'.format(math.sqrt(num)))
