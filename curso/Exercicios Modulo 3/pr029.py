"""
Calcular a Equação

S = 0 + 1/2 + 1/3 + 1/4 + ... + 1/n

"""

n = int(input('Digite o Numero de Parada: '))
s = 0
print(s)
for _ in range(2, n + 1):
    print('1/{}'.format(_))
    s += 1/_

print('S = {}'.format(s))
