"""
Criar uma funcao que cria uma sequecia de pontos de exclamacao
determiada pela variavel (quantity).

author:VictorDaedalus
"""


def printLine(quantity=5):
    for turn in range(1, quantity + 1):
        if turn == 1:
            print('!')
        else:
            print('!' * turn)


printLine()
