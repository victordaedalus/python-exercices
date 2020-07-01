valor1 = input()
valor2 = input()

valor1 = valor1.split()
valor2 = valor2.split()

total = (int(valor1[1]) * float(valor1[2])) + (int(valor2[1]) * float(valor2[2]))
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
