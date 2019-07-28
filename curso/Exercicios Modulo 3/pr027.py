"""
Calcular Um numero Harmonico

H(n) = 1 + 1/2 + 1/3 + 1/4 + ... 1/n

"""

n = int(input('n = '))
harmonico = 1
print(harmonico)
for _ in range(2, n + 1):
    print('1/{}'.format(_))
    harmonico += (1 / _)

print('H({}) = {}'.format(n, harmonico))
