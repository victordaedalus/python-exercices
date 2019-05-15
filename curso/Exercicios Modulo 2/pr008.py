print('Digite a primeira nota do aluno:')
nota1 = float(input())
print('Digite a segunda nota:')
nota2 = float(input())

if (0 <= nota1 <= 10) and (0 <= nota2 <= 0):
    print('A sua media é de {}'.format((nota1 + nota2) / 2))
else:
    print('Essas notas não são validas.')
