def semana(dia):
    dias = {
        1: 'Segunda',
        2: 'Terça',
        3: 'Quarta',
        4: 'Quinta',
        5: 'Sexta',
        6: 'Sabado',
        7: 'Domingo'
    }
    print('O dia da semana é {}'.format(dias[dia]))


print('Digite um numero de 1 a 8:')
number = int(input('> '))
if 1 <= number <= 8:
    semana(number)
else:
    print('Numero inválido')
