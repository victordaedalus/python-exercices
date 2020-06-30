"""
Função que receba uma data como:
10/10/2020

E apresente ela de modo extenso, como:

10 de Outubro de 2020
"""


def mes(mes):
    mes = int(mes)
    mes -= 1 
    meses = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril'
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro',
    ]
    return meses[mes]


def calendar(data):
    data = data.split('/')
    return f'{data[0]} de {mes(data[1])} de {data[2]}'


date = input('Digite a Data de Hoje: ')
print(calendar(date))
