"""
Criar um vetor com 10 valores e verificar se existem valores iguais, e mostrá-los na tela.
author:ghostborn67
"""

# Var
lista = []
repeticao = []

# Run
for i in range(1, 11):
    lista.append(int(input(f'{i}° $> ')))

for x in lista:
    if x in repeticao:
        pass
    else:
        if lista.count(x) > 1:
            repeticao.append(x)

print('A lista possui os seguintes valores iguais:')
print(repeticao)
