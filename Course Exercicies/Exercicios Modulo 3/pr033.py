"""
Imprimir 'n' numeros multiplos de 'i' e 'j'
author:ghostborn67
"""

counter = 1
n = int(input('n = '))
i = int(input('i = '))
j = int(input('j = '))
num = 1
print(80 * '\n')

while counter <= n:
    if (i % num) == 0 or (j % num) == 0:
        print(num)
        counter += 1
    elif (num % i) == 0 or (num % j) == 0:
        print(num)
        counter += 1
    num += 1
