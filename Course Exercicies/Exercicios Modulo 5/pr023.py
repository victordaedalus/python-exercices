"""
Criar uma funcao que mostra na tela um triangulo vertical.

author:VictorDaedalus
"""


def lateral_triangule(n):
    locker = True
    counter = 1

    if n == 1:
        print('*')
    else:
        while True:
            print('*' * counter)
            if counter < n and locker is True:
                counter += 1
                if counter == n:
                    counter += 1
                    locker = False
            if locker is False:
                counter -= 1
                if counter == 0:
                    break


lateral_triangule(10)

