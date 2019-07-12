"""
Calculador de Medias
author: ghostborn67
"""
contador_nota = 1
contador_media = 0
nota_final = 0

while True:
    # Para fazer com que pare de reconhecer notas, digitar numeros acima de 10 ou menores que 0
    nota = int(input('Digite a {} Nota: '.format(contador_nota)))
    if 0 < nota > 10:
        break
    contador_nota += 1
    contador_media += 1
    nota_final += nota

media = nota_final / contador_media
print('A Media foi de {}'.format(media))
