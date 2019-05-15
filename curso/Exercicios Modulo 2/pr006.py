print('Digite um numero:')
num1 = int(input())
print('Digite outro numero:')
num2 = int(input())
if num1 > num2:
    print('O numero {} é maior que o numero {}'.format(num1, num2))
    print('Com a diferença de {}'.format(num1 - num2))
else:
    print('O numero {} é maior que o numero {}'.format(num2, num1))
    print('Com a diferença de {}'.format(num2 - num1))
