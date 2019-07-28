print('Digite um ano:')
ano = int(input('> '))

if ano % 400:
    print('Esse ano é bissesto')
else:
    print('Esse ano não é bissesto')
