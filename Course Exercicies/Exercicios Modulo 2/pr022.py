print("""
###############################################################################
#                       Sistemas do Governo Federal                           #
#                         Teste de Aposentadoria                              #
###############################################################################



""")
print('Qual é a sua idade:')
idade = int(input('> '))
print('A quantos anos o senhor trabalha:')
traba = int(input('>  '))

if idade == 65 or traba == 30 or (idade == 65 and traba == 25):
    print('Aposentadoria Aprovada...')
else:
    print('Aposentadoria Reprovada...')
