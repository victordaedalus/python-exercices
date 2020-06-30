"""
Lista que armazene a media de 15 alunos e imprima a média geral.
author:ghostborn67
"""
vetor = []

for i in range(15):
    vetor.append(float(input(f'Digite a Nota do {i + 1}° aluno: ')))

media = sum(vetor) / 15

print(f'A média foi de {media} pontos.')
