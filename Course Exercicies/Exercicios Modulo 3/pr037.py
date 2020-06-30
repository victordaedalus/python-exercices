"""
Achar numeros de 1000 a 9999 com as propriedades seguintes:

3025
30 + 25 = 55
55² = 3025
"""

for i in range(1000, 10000):
    local = int(str(i)[0:2]) + int(str(i)[2:4])
    local = local ** 2
    if local == i:
        print(i)
