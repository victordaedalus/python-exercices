from math import sqrt

a = float(input('Digite o elemento A:'))
b = float(input('Digite o elemento B:'))
c = float(input('Digite o elemento C:'))

delta = b ** 2 - 4 * a * c

if delta > 0:
    print('Não existe raiz real.')
elif delta == 0:
    baska1 = (- b) / (2 * a)
    print('Raiz Unica, {}'.format(baska1))
else:
    baska1 = (- b + sqrt(delta)) / (2 * a)
    baska2 = (- b + sqrt(delta)) / (2 * a)
    print('[ {}, {} ]'.format(baska1, baska2))
