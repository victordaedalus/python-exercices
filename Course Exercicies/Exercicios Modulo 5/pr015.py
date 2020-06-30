"""
Programa que recebe 3 valores (obrigatoriamente maiores que 0) e calcula por meio de funcoes,
se os dados inseridos sao de um triangulo, e se for, ele revela o tipo do triangulo.

author:VictorDaedalus
"""
from jump import jump
from pr016 import DesenhaLinha


def tri_check(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def tri_category(a, b, c):
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    else:
        return 'Scalene'


while True:
    DesenhaLinha(20)
    side1 = float(input('Input the side1: '))
    side2 = float(input('Input the side2: '))
    side3 = float(input('Input the side3: '))
    DesenhaLinha(20)

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print('Data less than 0 is not allowed.')
    else:
        break


jump(5)

if tri_check(side1, side2, side3):
    print('The data passed is from a triangle.')
    print(f'The triangle shown is {tri_category(side1, side2, side3)}')
else:
    print('The entered data is not from a triangle')
