"""
Indentificar mes pelo equivalente numerico.
author: ghostborn67
"""


def mes(num):
    meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    return meses[num]


numero = int(input('Digite o numero correspondente ao mês:\n> '))
if 1 <= numero <= 12:
    print('O mes selecionado foi {}'.format(mes(numero)))
else:
    print('Numero Invalido...')
