"""
Criar dois vetores, onde o primeiro vai receber 10 valores reais,
e o segundo vai receber os 10 valores com cada um elevado ao quadrado.
@autor:ghostborn67
"""
from math import pow

list1 = []
list2 = []

for i in range(1, 11):
    list1.append(float(input(f'Digite o {i}° valor: ')))

for i in list1:
    list2.append(pow(i, 2))

print(list1)
print(list2)
