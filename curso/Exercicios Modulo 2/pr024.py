print("""
Para qual estado deseja enviar:
MG - 1
SP - 2
RJ - 3
MS - 4
""")
select_state = int(input('> '))
valor = float(input('Qual é o valor financeiro enviado:\n> '))

if select_state == 1:
    print('O preço final foi de {}'.format((valor * 7 / 100) + valor))
elif select_state == 2:
    print('O preço final foi de {}'.format((valor * 12 / 100) + valor))
elif select_state == 3:
    print('O preço final foi de {}'.format((valor * 15 / 100) + valor))
elif select_state == 4:
    print('O preço final foi de {}'.format((valor * 8 / 100) + valor))
else:
    print('Estado Invalido, tente novamente...')
