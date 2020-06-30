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
    print(f'O dia da semana é {dias[dia]}')


print('Digite um numero de 1 a 7:')
number = int(input('> '))
if number <= 7:
    semana(number)
else:
    print('Numero inválido')
