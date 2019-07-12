notas = 0

for i in range(10):
    local_notas = int(input('Digite a {}º nota: '.format(i + 1)))
    notas += local_notas

media = notas / 10
print('A media foi de {}'.format(media))
