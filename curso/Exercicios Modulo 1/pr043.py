print('Qual é o valor a ser trabalhado:')
valor = float(input())
vista_desconto = valor - (valor * 100 / 10)
parcela3 = valor / 3
vend_vist = vista_desconto / 100 * 5
vend_par = parcela3 / 100 * 5
print('O Valor a Vista fica com R${}'.format(vista_desconto))
print('Com a comição de R${}'.format(vend_vist))
print('O Valor das parcelas é de R${}'.format(parcela3))
print('Com a comição de R${}'.format(vend_par))
