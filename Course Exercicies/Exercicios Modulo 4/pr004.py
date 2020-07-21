lista = []
for i in range(8):
    lista.append(int(input(f'Digite o {i + 1}° Numero: ')))

x = int(input('Digite a posição X: '))
y = int(input('Digite a posição y: '))

if x <= 7 or y <= 7:
    soma = lista[x] + lista[y]
    print(f'A soma é igual a {soma}')
else:
    print('Valores Invalidos.')

