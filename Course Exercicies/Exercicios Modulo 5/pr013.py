"""
Fazer uma função que receba 2 valores numericos e um simbolo, e com a variação do simbolo,
mudar o tipo de operação realizada pela função.

author:VictorDaedalus
"""


def calculator(num1, num2, token='+'):
    if token == '+':
        return num1 + num2
    elif token == '-':
        return num1 - num2
    elif token == '*':
        return num1 * num2
    elif token == '/':
        return num1 / num2

print(calculator(12, 17))
