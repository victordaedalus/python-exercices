"""
Fazer um função que receba os KM percorridos e o Litros consumidos, e calcule o KM/L e dependedo
do resultado, mostrar uma mensagem especifica.

author:VictorDaedalus
"""


def consumo(km, l):
    consum = km / l

    if consum < 8:
        print('Venda o Carro!')
    elif 8 <= consum <= 12:
        print('Econômico!')
    else:
        print('Super Econômico!!!')


consumo(16, 1)