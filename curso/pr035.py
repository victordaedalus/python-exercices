from math import sqrt, pow


print('Digite o valor do cateto A:')
print('Digite o valor do cateto B:')
a = float(input())
b = float(input())

data = sqrt(pow(a, 2) + pow(b, 2))
print('O valor da hiptenusa é de {}'.format(data))
