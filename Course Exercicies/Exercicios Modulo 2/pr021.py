print("""
Escolha uma Opção:
1 = Soma de Dois Numeros
2 = Diferença entre dois numeros
3 = Produto de Dois Numeros
4 = Divisão entre Dois Numeros

""")

opc = int(input('#> '))

if opc == 1:
    x = int(input('Digite o primero numero da soma:'))
    y = int(input('Digite o segundo nunero da soma:'))
    print('O resultado da soma foi de {}'.format(x + y))
elif opc == 2:
    x = int(input('Digite o primero numero:'))
    y = int(input('Digite o segundo nunero:'))
    if x > y:
        z = x - y
    else:
        z = y - x
    print('A diferença entre os numero é de {}'.format(z))
elif opc == 3:
    x = int(input('Digite o primero numero:'))
    y = int(input('Digite o segundo nunero:'))
    print('O produto foi de {}'.format(x * y))
elif opc == 4:
    x = int(input('Digite o Dividendo (Não pode ser igual a 0.):'))
    y = int(input('Digite o Divisor:'))
    print('O quociente foi de {}'.format(x / y))
