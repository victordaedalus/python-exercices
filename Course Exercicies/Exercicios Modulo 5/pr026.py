"""
Criar uma funcao que realiza um somatiorio ate a variavel final.

author:VictorDaedalus
"""


def summation(final):
    counter = 1
    result = 0
    while counter <= final:
        result += counter
        counter += 1
    
    return result


print(summation(5))