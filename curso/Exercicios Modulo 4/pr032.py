"""
Receber dois vetores X e Y que recebam 5 números cada e calcule:

1.Soma entre cada numero da mesma posição de X e Y.
2.Produto da Multiplicação entre cada numero da mesma posição de X e Y.
3.Diferença de X em Y (Mostrar todos os numeros de X que não existem em Y).
4.Intersecção de X e Y
5.União de X e Y

author:ghostborn67
"""

x = []
y = []

base = []

for i in range(5):
    x.append(int(input(f'Digite o {i + 1}° número do X: ')))

for i in range(5):
    y.append(int(input(f'Digite o {i + 1}° número do Y: ')))

# Soma entre cada numero da mesma posição de X e Y.
for i in range(5):
    print()
    base.append(x[i] + y[i])

print('A soma de de X e Y é de:')
print(base)
base = []

# Produto da Multiplicação entre cada numero da mesma posição de X e Y.
for i in range(5):
    base.append(x[i] * y[i])

print('O produto de de X e Y é de:')
print(base)
base = []

# Diferença de X em Y (Mostrar todos os numeros de X que não existem em Y).
for item in x:
    if item not in y:
        base.append(item)

print('Os Itens de X que não estão em Y são:')
print(base)

# Intersecção de X e Y
print('A Intersecção entre X e Y é:')
print(set(x).intersection(y))

# União entre X e Y
print('A União entre X e Y é:')
print(set(x).union(y))
