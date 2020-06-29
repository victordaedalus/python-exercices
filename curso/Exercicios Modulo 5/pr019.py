"""
Fazer uma funcao que mostre o maior numero primo de um determinado numero.

author:VictorDaedalus
"""


def high_prime(number):
    bigger = 0
    for x in range(1, number + 1):
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
            if x > bigger:
                bigger = x
    return bigger


print(high_prime(100))
