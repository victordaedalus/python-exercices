print('Digite um numero:')
numero = int(input())
processo = str(numero)

if 1 <= numero <= 10:
    print(int(processo[0]))
elif 10 <= numero <= 100:
    print(int(processo[0]) + int(processo[1]))
elif 100 <= numero <= 1000:
    print(int(processo[0]) + int(processo[1]) + int(processo[2]))
elif 1000 <= numero <= 10000:
    print(int(processo[0]) + int(processo[1]) + int(processo[2]) + int(processo[3]))
