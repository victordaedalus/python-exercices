"""
Calcular a Equação

E = 1 + 1/1 + 1/2 + 1/3 + 1/4 ... + 1/n,

"""

n = int(input('n = '))
e = 1
print(e)
for _ in range(1, n + 1):
    print('1/{}'.format(_))
    e += (1 / _)

print('E = {}'.format(e))
