"""
Teste de comparação de numeros
author: ghostborn67
"""
base_h = 0
base_l = 0

for _ in range(10):
    nun = int(input('$> '))
    if nun > base_h:
        base_h = nun
    if nun < base_l:
        base_l = nun

print("""
O Maior Numero Foi {}.
O Menor Numero Foi {}.
""".format(base_h, base_l))
