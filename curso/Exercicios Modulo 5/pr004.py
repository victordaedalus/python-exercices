"""
Função que indentifica numeros quadrados perfeitos, sendo esses 
não negativos e são o quadrado de outro numero.
author:VictorDaedalus
"""


def perfectsquare(sq):
    if sq <= 0:
        return False
    else:
        # O Principio do problema é fazer com o que a maquina compare vários números menores que o "sq" entregue para assim por meio de comparações, descobrir se o numero é um potenciação
        for number in range(1, sq + 1):
            if number * number == sq:
                return True
            elif number is sq:
                return False


print(perfectsquare(int(input('#> '))))