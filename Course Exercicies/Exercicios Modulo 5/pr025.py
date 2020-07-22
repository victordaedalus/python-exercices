"""
Criar uma funcao que calcula uma determinada serie numerica ate um determinado ponto.

author:VictorDaedalus
"""

def series(variable):
    serie = 0
    for turn in range(1, variable + 1):
        serie += (turn ** 2 + 1) / (turn + 3)
    
    return serie


print(series(5))
