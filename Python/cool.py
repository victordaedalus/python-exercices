"""
That is a simple script!!
author: Victor D. C. Cardoso
"""

#Imports
from time import sleep

#Execution
name = input('What is your name? \n>') ; print('')
print('Interesting... {} right!?'.format(name))

print('For YES print(1), For NO Print(2)...')
question = int(input('$ '))

if question == 1:
    print('OK...')
    sleep(5)
    print('But...')
    sleep(2)
    print('I am thinking here...')
    sleep(2)
    print('Is better you not enter here...')
    sleep(3)
    print('at least for now...')
    sleep(1)
    print('Believe me...')
    sleep(5)
    print('You are NOT really ready...')
    sleep(7)
    print('..yet.')
    sleep(2)
    print('Well... Comeback later!')
    sleep(0.7)
    print('Bye!!')


elif question == 2:
    print('Ok... you are not him.. right?')
    sleep(3)
    print('...')
    sleep(4)
    print('....')
    sleep(5)
    print('fine... Just go away...')
    exit()

