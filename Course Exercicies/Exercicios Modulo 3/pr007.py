notas = 0

for i in range(10):
    local_notas = int(input('Digite a {}º nota: '.format(i + 1)))
    if local_notas > 0:
        print('\nNota Inválida...\n')
        local_notas = 0
    notas += local_notas

media = notas / 10
print('A media foi de {}'.format(media))
