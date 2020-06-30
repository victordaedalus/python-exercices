"""
Calcular as Sequencias Numerias

A = 1 + 2 + 3 + 4 + 5 + 6 + ... + n
B = 1 - 2 + 3 - 4 + 5 - 6 + ... + (2n - 1)
C = 1 + 3 + 5 + 7 + 9 + 11 + ... + (2n - 1)
"""

n = int(input('n = '))
a, b, c = 1, 1, 0

for i in range(2, n + 1):
    a += i

counter = True
for i in range(2, n + 1):
    if i != n:
        if counter is True:
            b -= i
            counter = False
        elif counter is False:
            b += i
            counter = True
    else:
        b = (2 * n - 1)

for i in range(1, n + 1, 2):
    if i != n:
        c += i
    else:
        c += (2 * n - 1)

print('''
A = {}
B = {}
C = {}
'''.format(a, b, c))
