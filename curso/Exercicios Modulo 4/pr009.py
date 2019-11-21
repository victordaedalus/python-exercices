"""
Criar um vetor que receberá 6 números pares e imprimir o mesmo inversamente.
author:ghostborn67
"""
# Variables
lista = []

# Run
for i in range(6):
    num = int(input(f'Digite o {i + 1}° numero: '))
    while True:
        if num % 2 == 0:
            lista.append(num)
            break
        else:
            print('Numero Impar, digite outro')
            num = int(input(f'Digite o {i + 1}° numero: '))

lista.reverse()
print(lista)
