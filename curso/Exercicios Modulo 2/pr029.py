"""
Sistema de provas por terminal
author:ghostborn67
"""
from random import randrange
from time import sleep


# Gerador de questões
questaoA1 = randrange(1, 101)
questaoA2 = randrange(1, 101)
questaoB1 = randrange(1, 101)
questaoB2 = randrange(1, 101)
questaoC1 = randrange(1, 101)
questaoC2 = randrange(1, 101)
questaoD1 = randrange(1, 101)
questaoD2 = randrange(1, 101)
questaoE1 = randrange(1, 101)
questaoE2 = randrange(1, 101)
placar = 0

# Execução

rA = int(input('{} + {} = '.format(questaoA1, questaoA2)))
rB = int(input('{} + {} = '.format(questaoB1, questaoB2)))
rC = int(input('{} + {} = '.format(questaoC1, questaoC2)))
rD = int(input('{} + {} = '.format(questaoD1, questaoD2)))
rE = int(input('{} + {} = '.format(questaoE1, questaoE2)))

if rA == questaoA1 + questaoA2:
    print('Voce acertou a questão A!!')
    placar = placar + 1
    sleep(3)
if rB == questaoB1 + questaoB2:
    print('Voce acertou a questão B!!')
    placar = placar + 1
    sleep(3)
if rC == questaoC1 + questaoC2:
    print('Voce acertou a questão C!!')
    placar = placar + 1
    sleep(3)
if rD == questaoD1 + questaoD2:
    print('Voce acertou a questão D!!')
    placar = placar + 1
    sleep(3)
if rE == questaoE1 + questaoE2:
    print('Voce acertou a questão E!!')
    placar = placar + 1
    sleep(3)

print(20 * '\n', 'Você acertou {} questões'.format(placar))
