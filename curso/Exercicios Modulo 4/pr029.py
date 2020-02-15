"""
Fazer um programa que receba 6 numeros e mostre:

Os números pares digitados e a soma deles.
Os números impares digitados e a soma deles.

author:ghostborn67
"""

vetor = []
par = []
impar = []

count = 1
while count <= 6:
    vetor.append(int(input(f'Digite o {count}° número: ')))
    count += 1

for i in vetor:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"""
Os números pares digitados foram:
{par}
Eles possuem a soma total de {sum(par)}

Os números impares digitados foram:
{impar}
Eles possuem a soma total de {sum(impar)}
""")
