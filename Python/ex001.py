"""
Ficha de Pessoa Fisica, Exercise 001
Itens Pedidos: nome, cpf, endereço, idade, altura, telefone
author: Victor D. C Cardoso
"""

#Imports
from time import sleep

#Variaveis e execução

print("############################################")
print('#          Ficha Formulario Brasil         #')
print('############################################')
print(' ')

name = input('Digite o seu Nome:\n> ')
print('')
cpf = input('Digite o seu CPF:\n> ')
print('')
end = input('Digite o seu Endereço:\n> ')
print('')
idade = input('Digite a sua Idade:\n> ')
print('')
alt = input('Digite a sua Altura:\n> ')
print('')
tel = input('Digite o seu Telefone:\n> ')
print(20 * '\n')

print('#################################')
print('#  Processando Informações...   #')
print('#################################')
sleep(4)
print(30 * '\n')

print('#################################')
print('#    Formulario do Usuario:     #')
print('#################################')

print('Nome do Usuário:\n$ {}'.format(name))
print('')
print('CPF do Usuário:\n$ {}'.format(name))
print('')
print('Endereço do Usuario:\n$ {}'.format(end))
print('')
print('Idade do Usuário:\n$ {}anos'.format(idade))
print('')
print('Altura do Usuário:\n$ {}m'.format(alt))
print('')
print('Telefone do Usuário\n$ {}'.format(tel))
