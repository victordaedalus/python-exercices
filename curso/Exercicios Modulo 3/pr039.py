"""
Area do Triangulo

A = b * h / 2
"""

while True:
    b = int(input('Digite a Base do Triangulo: '))
    h = int(input('Digite a Altura do Triangulo: '))
    if b < 0 or h < 0:
        print('Numeros Invalidos')
    else:
        print(f'Area = {(b * h) / 2}')
        break
