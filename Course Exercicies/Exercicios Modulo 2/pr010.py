print('Digite a altura:')
altura = float(input())
print('Digite o sexo (1)=Homens (2)=Mulheres')
sexo = int(input())
if sexo == 1:
    ideal = (72.7 * altura) - 58
    print('A peso ideal é de {}'.format(ideal))
else:
    ideal = (62.1 * altura) - 44.7
    print('A peso ideal é de {}'.format(ideal))
