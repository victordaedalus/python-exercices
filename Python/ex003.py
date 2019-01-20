"""
String and List Manipulation Script
author:DarkBorn
"""
# Imports


# Variaveis
string = str()
lista = ['Victor', 'Alfredo', 'Dreffus', 2, 2.4]

# Execução
print('Com o que você deseja trabalhar? ')
print('1 para String, 2 para List')
valor = int(input('$> '))
print('')

if valor == 1:
    string = str(input('Digite uma String:\n$> '))
    print('Ela possui {} caracteres...\n'.format(len(string)))
    print('A string minuscula:\n{}\n'.format(string.upper()))
    print('A string MAIUSCULA:\n{}\n'.format(string.upper()))
    str_list = string.split(' ')
    print('A String Como Lista:\n{}\n'.format(str_list))

elif valor == 2:
    print('A Lista Atual é:\n{}\n'.format(lista))
    obj = input('Adicione um Objeto a Lista:\n$> ')
    lista.append(obj)
    print('')
    remov = input('Remova um Item da Lista:\n$> ')
    lista.remove(remov)
    print('')
    print('A Lista Final Ficou Assim:\n{}\n'.format(lista))

print('\nObrigado Por Usar o Script!!!\n\n\n')
