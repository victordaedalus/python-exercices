print('Digite o primeiro numero:')
num1 = int(input())
print('Digite outro numero:')
num2 = int(input())
if num1 > num2:
    print('O numero {} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('O numero {} é maior que {}'.format(num2, num1))
else:
    print('O dois numeros são iguais...')
