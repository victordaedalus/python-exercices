"""
Calcular R = (R1 * R2) / (R1 + R2)
Até que um valor seja igual a 0
"""
from time import sleep


while True:
    r1 = int(input('Digite o valor R1: '))
    r2 = int(input('Digite o valor R2: '))

    if r1 == 0 or r2 == 0:
        break

    r = (r1 * r2) / (r1 + r2)
    print(f'R = {r}')
    sleep(4)
