"""
Calcular a seguinte formula:

S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

S = nun1/ nun2
"""

# Var
nun1 = 1
nun2 = 1
s = 0
# Exec

print('{}/{}'.format(nun1, nun2))

while True:
    nun1 += 2
    nun2 += 1
    print('{}/{}'.format(nun1, nun2))
    s = nun1 / nun2

    # Verificação para saber se ainda está detro da equação
    if nun1 >= 99 and nun2 >= 50:
        break

print('S = {}'.format(s))
