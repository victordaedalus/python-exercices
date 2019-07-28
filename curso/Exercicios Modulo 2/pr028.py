from fractions import Fraction

x = float(input('Digite a variavel X: '))
y = float(input('Digite a variavel Y: '))
z = float(input('Digite a variavel Z: '))
print((20 * '\n'), """
Escolha a opção de media:
1 - Média Geometrica
2 - Média Poderada
3 - Média Harmonica
4 - Média Aritimetica
\n
\n
""")
choice = int(input('> '))

if choice == 1:
    med = round((x * y * z) ** (1/3))
    print(20 * '\n', 'Sua Media foi de {}'.format(med))
elif choice == 2:
    med = (x + 2 * y + 3 * z) / 6
    print(20 * '\n', 'Sua Media foi de {}'.format(med))
elif choice == 3:
    med = 1 / (Fraction(1, x) + Fraction(1, y) + Fraction(1, z))
    print(20 * '\n', 'Sua Media foi de {}'.format(med))
elif choice == 4:
    med = (x + y + z) / 3
    print(20 * '\n', 'Sua Media foi de {}'.format(med))
else:
    print('Opção invalida!!')
