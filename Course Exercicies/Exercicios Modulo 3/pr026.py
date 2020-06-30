"""
Entontrar numero multiplo de 11, 13 ou 17
"""

num = int(input('Digite um numero: '))
select = num
while True:
    select += 1
    if (select % 11) == 0 or (select % 13) == 0 or (select % 17) == 0:
        print('O numero selecionado foi {}'.format(select))
        break
