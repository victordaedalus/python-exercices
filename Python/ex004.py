"""
Programa de Gerenciamento de Convidados.

Receive: Nº de Convidados, Nomes dos Convidados
Return: Lista Organizada e Numerada de Convidados 
author: Victor D. C. C.
"""

# Imports


# Variables
number_guest = 0
guest_names = []
guest = ''
au_var = 0

# Execution
print('#####################################################')
print('#     Programa de Gerenciamento de Convidados.      #')
print('#####################################################\n')

number_guest = int(input('Digite a Quantidade de Convidados: '))
print('')

for i in range(number_guest):
    au_var += 1
    guest = input('Digite o nome do {}º Convidado:\n&> '.format(au_var))
    guest_names.append(guest)
    print('')

print(30 * '\n')

au_var = 0

for people in guest_names:
    au_var += 1
    print('{}º Convidado: {}'.format(au_var, people))

print('\n Obridado Por Usar Nosso Programa')
