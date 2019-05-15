"""
Teste de numero divisivel por 3 e 5
author: Ghostborn67
"""


def retorno(number, div):
    local_number = number % div
    if local_number == 0:
        return True
    else:
        return False


numero = int(input('Digite um numero inteiro:'))

if retorno(numero, 3) and retorno(numero, 5):
    print('Numero invalido...')
    print('Numero divisivel por 3 e 5')
elif retorno(numero, 3):
    print('Esse numero é divisivel por 3')
elif retorno(numero, 5):
    print('Esse numero é divisivel por 5')
else:
    print('Esse numero é não divisivel por nenhuma das opções validas.')
