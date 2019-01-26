"""
Algoritmo de Calculo de Média Bimestral
Recebe: Nomes, 2 Notas
Retorna: Lista de Alunos com Media
"""
# Imports


# Variables
num_alunos = 0
nome_aluno = []
nota1 = []
nota2 = []
media = []
aprovação = ''
au_var1 = ''  # Variavel Auxiliar de nome_alunos
au_var2 = 0.0  # Variavel Auxiliar de nota1
au_var3 = 0.0  # Variavel Auxiliar de nota2
au_var4 = 0.0  # Variavel Auxiliar de media
au_var_num = 0  # Variavel Auxiliar de Numero dos Alunos
au_var_num2 = 0  # Variavel Auxiliar de Numero dos Alunos

# Execution
print('#################################')
print('#   Terminal de Media Bimestral #')
print('#################################\n')

num_alunos = int(input('Digite a Quantidade de Alunos da Sala: '))

for i in range(num_alunos):
    print(3 * '\n')
    au_var_num += 1
    au_var_num2 = au_var_num - 1

    au_var1 = input('Digite o Nome do {}º Aluno: '.format(au_var_num))
    nome_aluno.append(au_var1)

    print('\nNotas do {} ºAluno: {}\n'.format(
        au_var_num, nome_aluno[au_var_num2]))

    au_var2 = float(input('Digite a 1º Nota do Aluno: '))
    nota1.append(au_var2)

    au_var3 = float(input('Digite a 2º Nota do Aluno: '))
    nota2.append(au_var3)

    au_var4 = (au_var2 + au_var3) / 2
    media.append(au_var4)
print(20 * '\n')
print("###############################################################")
print('############            Lista de Alunos            ############')
print("###############################################################")
au_var_num = 1

while au_var_num <= num_alunos:
    au_var_num2 = au_var_num - 1
    au_var1 = nome_aluno[au_var_num2]
    au_var2 = nota1[au_var_num2]
    au_var3 = nota2[au_var_num2]
    au_var4 = media[au_var_num2]

    if au_var4 >= 6.0:
        aprovação = 'Aprovado'
    else:
        aprovação = 'Desaprovado'

    print('{}º Aluno /{}/ 1ºNota = {} , 2ºNota = {}, Media = {}/ {} /\n'.format(
        au_var_num, au_var1, au_var2, au_var3, au_var4, aprovação))

    au_var_num += 1
