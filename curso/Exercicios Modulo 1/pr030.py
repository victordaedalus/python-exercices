cota = float(input('Qual é a cotação do dolar: '))
real = float(input('Quantos Reais deseja converter: '))
convertido = real / cota
print('BRL{} = US${}'.format(real, convertido))
