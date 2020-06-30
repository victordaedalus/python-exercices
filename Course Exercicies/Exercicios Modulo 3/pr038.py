"""
Calcular a² + b² = c²
a + b + c = 1000


##################
#    Internet    #
##################

s = 1000
stop = False
for a in range(1, int(s / 3)):
    for b in range(1, int(s / 2)):
        c = s - a - b
        if a*a + b*b == c*c:
            print(f'A = {a}, B = {b}, C = {c}')
            stop = True
            break
    if stop is True:
        break

"""

###########
#  pr038  #
###########

counter = False

for a in range(1, 1001):
    for b in range(a + 1, a + 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f'A={a} B={b} C={c}')
            counter = True
            break
    if counter is True:
        break
