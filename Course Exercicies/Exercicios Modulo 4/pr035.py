"""
Ler dois numeros A e B (positivos e menores que 10000) e:

- Crie um vetor onde cada posição é um algarismo do numero.
- Crie um vetor que seja a soma entre A e B, mas faça usando os vetores anteriores.

author:ghostborn67
"""

a = input('Digite o Numero A: ')
b = input('Digite o Numero B: ')
alist = []
blist = []
final = []
counters = {'counterA': None, 'counterB': None}

# Criar As Listas.
for alg in a:
    alist.append(int(alg))

for alg in b:
    blist.append(int(alg))

# Forma de manter a lista.
counterA = -1
counterB = -1
meter = 1

#  Fazer a soma das Listas.
for i in list(range(-1, -6))[::-1]:

       
    


"""
ia = counter

while calcu <= counter:
    if lock is True:
        base = alist[i] + blist[i] + 1
        lock = False
    else:
        base = alist[i] + blist[i]

    if base > 10:
        diferenca = base - 10
        lock = True
        final.append(diferenca)
    else:
        final.append(base)

if meter == len(alist) or meter == len(blist):
       
    else:
        final.append(alist[counterA] + blist[counterB])
        counterA -= 1
        counterB -= 1
        meter += 1

    
"""
final.reverse()
print(final)
