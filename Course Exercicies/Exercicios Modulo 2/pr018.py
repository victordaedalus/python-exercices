"""
Calculadora
author:ghostborn67
"""

print('''
Qual operação deseja fazer:
1 (adição)
2 (subtração)
3 (multiplicação)
4 (divisão)
''')

select = int(input('$> '))

if select == 1:
    x = int(input('Digite o primeiro elemento da adição: '))
    y = int(input('Digite o segundo elemento da adição: '))
    print('{} + {} = {}'.format(x, y, x + y))
if select == 2:
    x = int(input('Digite o primeiro elemento da subtração: '))
    y = int(input('Digite o segundo elemento da subtração: '))
    print('{} - {} = {}'.format(x, y, x - y))
if select == 3:
    x = int(input('Digite o primeiro elemento da multiplicação: '))
    y = int(input('Digite o segundo elemento da multiplicação: '))
    print('{} * {} = {}'.format(x, y, x * y))
if select == 3:
    x = int(input('Digite o primeiro elemento da divisão: '))
    y = int(input('Digite o segundo elemento da divisão: '))
    print('{} / {} = {}'.format(x, y, x / y))
