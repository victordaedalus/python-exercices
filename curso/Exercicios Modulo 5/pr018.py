"""
Fazer uma funcao que realiza uma exponenciacao sem usar nem uma outra funcao.\

author:VictorDaedalus
"""

def plusNumber(x=2, z=2):
    return x ** z


principia = int(input('principia #> '))
plus = int(input('plus #> '))

print(plusNumber(principia, plus))
