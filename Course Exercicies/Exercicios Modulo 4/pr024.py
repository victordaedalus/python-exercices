"""
Criar um programa que leia 10 conjuntos com 2 valores cada sendo o primeiro valor o numero do aluno,
e o segundo sua altura, e após isso mostrar na tela o maior aluno e seu numero assim tambem como o menor.
author:ghostborn67
"""

alunoA, alunoB, alunoC = [], [], []
alunoD, alunoE, alunoF = [], [], []
alunoG, alunoH, alunoI, alunoJ = [], [], [], []
lista_alunos = []
menor = {'Altura': None, 'Numero': None}
maior = {'Altura': None, 'Numero': None}

alunoA.append(int(input('Digite o Numero do Aluno: ')))
alunoA.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoA)
print('\n')

alunoB.append(int(input('Digite o Numero do Aluno: ')))
alunoB.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoB)
print('\n')

alunoC.append(int(input('Digite o Numero do Aluno: ')))
alunoC.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoC)
print('\n')

alunoD.append(int(input('Digite o Numero do Aluno: ')))
alunoD.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoD)
print('\n')

alunoE.append(int(input('Digite o Numero do Aluno: ')))
alunoE.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoE)
print('\n')

alunoF.append(int(input('Digite o Numero do Aluno: ')))
alunoF.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoF)
print('\n')

alunoG.append(int(input('Digite o Numero do Aluno: ')))
alunoG.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoG)
print('\n')

alunoH.append(int(input('Digite o Numero do Aluno: ')))
alunoH.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoH)
print('\n')

alunoI.append(int(input('Digite o Numero do Aluno: ')))
alunoI.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoI)
print('\n')

alunoJ.append(int(input('Digite o Numero do Aluno: ')))
alunoJ.append(float(input('Digite a Altura do Aluno: ')))
lista_alunos.append(alunoJ)
print('\n')

for aluno in lista_alunos:
    if maior['Altura'] is None:
        maior['Altura'] = aluno[1]
        maior['Numero'] = aluno[0]
    elif aluno[1] > maior['Altura']:
        maior['Altura'] = aluno[1]
        maior['Numero'] = aluno[0]

    if menor['Altura'] is None:
        menor['Altura'] = aluno[1]
        menor['Numero'] = aluno[0]
    elif aluno[1] < menor['Altura']:
        menor['Altura'] = aluno[1]
        menor['Numero'] = aluno[0]

print(f"""
Maior Aluno:
Numero:{maior['Numero']}
Altura:{maior['Altura']}

Menor Aluno:
Numero:{menor['Numero']}
Altura:{menor['Altura']}
""")
