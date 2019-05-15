print('Digite um numero entre 1000 e 9999:')
number = int(input())
if 1000 <= number <= 9999:
    number = str(number)
    print(number[0])
    print(number[1])
    print(number[2])
    print(number[3])
else:
    print('Numero invalido...')
