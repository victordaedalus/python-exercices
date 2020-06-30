print('Digite o valor da Nota 1:')
nota1 = float(input())
print('Digite o valor da Nota 2:')
nota2 = float(input())
print('Digite o valor da Nota 3:')
nota3 = float(input())

key = (nota1 + nota2 + nota3) / 3

if 0 <= key <= 10:
    final = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    if 0 <= key <= 10:
        print('Aluno reprovado / Nota {}'.format(final))
    else:
        print('Aluno aprovado / Nota {}'.format(final))
else:
    print('Notas Invalidas...')
