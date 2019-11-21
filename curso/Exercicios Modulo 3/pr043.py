"""
Ler um numero indefinido de idades, e calcular a media de idade do grupo.
Parar de ler idades ao ler idade = 0
"""
idades = 0
pessoas = 1
while True:
    local = int(input(f'Digite a idade da {pessoas}° pessoa: '))
    if local != 0:
        idades += local
        pessoas += 1
    else:
        break

media = int(idades / pessoas)
print(f'A idade media dessa {pessoas} pessoas, foi de {media} anos.')
