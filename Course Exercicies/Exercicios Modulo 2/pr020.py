a = float(input('Digite o comprimento do lado A:'))
b = float(input('Digite o comprimento do lado B:'))
c = float(input('Digite o comprimento do lado C:'))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Esse é um triangulo Equilátero.')
    elif a == b or a == c or b == c:
        print('Esse é um triangulo Isósceles.')
    else:
        print('Esse é um triangulo Escaleno.')
else:
    print('Valores não correspondentes a um triangulo')
