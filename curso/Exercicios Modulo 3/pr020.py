def par(x):
    if (x % 2) == 0:
        return 'Esse Numero é Par'
    else:
        return 'Esse Numero é Impar'


contador = 0
for i in range(1, 1001):
    print(i)
    print(par(i))
    if par(i) == 'Esse Numero é Par':
        contador += 1

print(20 * '\n')
print('Ele possuia {} numeros pares'.format(contador))
