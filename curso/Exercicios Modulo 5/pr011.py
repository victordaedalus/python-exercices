"""
Fazer um função que receba 4 valores, sendo esses:
3 notas e uma letra.

Se a letra for 'a', se deve calcular a média aritimética do aluno.
Se a letra for 'p', se deve calcular a média ponderada do aluno.
(Com pesos 5, 3, 2)

author:VictorDaedalus
"""


def average(nota1, nota2, nota3, tipo='a'):
    if tipo == 'a':
        return (nota1 + nota2 + nota3) / 3
    elif tipo == 'p':
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
    else:
        print('A Opção Selecionada é Inválida.')


print('{:.2f}'.format(average(8.4, 5.3, 7)))
