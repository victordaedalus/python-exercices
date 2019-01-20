"""
Script das Forças Armadas Brasileiras
author:DarkBorn
Requrimentos: 70kg, 1.80m , 18anos
"""

print('#############################################')
print('#   Programa de Seleção das Forças Armadas  #')
print('#############################################\n')

name = input('Qual é o Seu Nome:\n > ')
print('')
idade = int(input('Qual é a Sua Idade:\n > '))
print('')
peso = float(input('Qual é o Seu Peso:\n > '))
print('')
altura = float(input('Qual é a Sua Altura:\n > '))
print('')

if idade >= 18 and peso >= 70 and altura >= 1.8:
    print('Parabens {} Você está apto a entrar as Forças Armadas'.format(name))
else:
    print('Lamento {}...'.format(name))
    print('Você não está apto a entrar as Forças Armadas...')
