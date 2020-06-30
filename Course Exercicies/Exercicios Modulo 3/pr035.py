"""
Numeros Impares em um intervalo determinado pelo usuario
author:ghostborn67
"""


def v_par(x):
    if(x % 2) == 0:
        return True
    else:
        return False


soma = 0
inicio = int(input('Qual é o inicio do intervalo: '))
final = int(input('Qual é o final do intervalo: '))

if inicio < final:
    for i in range(inicio, final):
        if v_par(i) is False:
            soma += i
            print(i)

    print(f'Soma de Numeros Impares = {soma}')
else:
    print('Sequencia de Numeros Inválida.')
