"""
Def Função de Maior e Menor
author: GhostBorn67
"""
# Imports

# New Defs


def maior(colection):
    maior_item = colection[0]
    for item in colection:
        if maior_item < item:
            maior_item = item
    return maior_item


def menor(colection):
    menor_item = colection[0]
    for item in colection:
        if menor_item > item:
            menor_item = item
    return menor_item


# Variable
lista = []
var = True
au_var = 0
# Execution

while var == True:
    lista.append(int(input('Digite um Numero: ')))
    print('Para adicionar um novo numero, digite 1.')
    print('Para não adicionar um novo numero, digite 2.\n')
    au_var = int(input('&> '))
    if au_var >= 2:
        var = False

print('Você deseja saber o Maior(01) ou o Menor(02).')
au_var = int(input('&> '))

if au_var == 1:
    print(maior(lista))
else:
    print(menor(lista))
