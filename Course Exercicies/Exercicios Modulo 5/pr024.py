"""
Funcao que cria um um triangulo Horizontal de N lados, com a base igual a 2*N-1

author:VictorDaedalus
"""


def horizontal_tri(primal_number):
    tri_base = 2 * primal_number - 1
    space = int(tri_base / 2)
    sigil_counter = 0

    for turn in range(primal_number):
        print(space * ' ', (1 + (sigil_counter * 2)) * '*', space * ' ')
        space -= 1
        sigil_counter += 1


horizontal_tri(7)