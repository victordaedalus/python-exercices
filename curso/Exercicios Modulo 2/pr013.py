nota1 = float(input('Digite a nota da primeira prova:\n> '))
nota2 = float(input('Digite a nota da segunda prova:\n> '))
nota3 = float(input('Digite a nota da terceira prova:\n> '))

final = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 3

if final >= 6:
    print('Aluno aprovado...')
    print('Nota {}'.format(final))
else:
    print('Aluno reprovado...')
    print('Nota {}'.format(final))
