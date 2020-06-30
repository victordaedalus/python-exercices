"""
Escrever um vetor A que receba 10 elementos que obrigatoriamente devem estar entre 0 e 50,
e após isso criar outro vetor B que receba todos os numeros impares do vetor A,
E ao final mostrar os dois vetor, com dois elementos por linha.

author:ghostborn67
"""


def par(number):
    if number % 2 == 0:
        return True
    else:
        return False


vetorA = []
vetorB = []
counter = 1
counter2 = 0

print('Digite Numeros de 0 a 50:')
for i in range(10):
    nun = int(input(f'Digite o {i + 1}º numero: '))
    if 0 <= nun <= 50:
        vetorA.append(nun)
    else:
        while True:
            print('Número Incorreto:')
            nun = int(input(f'Digite o {i + 1}º numero: '))
            if 50 >= nun >= 0:
                vetorA.append(nun)
                break

for x in vetorA:
    if par(x) is False:
        vetorB.append(x)

print(vetorA)
print(vetorB)

print('Vetor A:')
while counter <= 5:
    counter2 += 1
    print(vetorA[counter2-1:counter2+1])
    counter2 += 1
    counter += 1

counter2 = 1

print('Vetor B:')
for i in range(vetorB.index(vetorB[-1])):
    print(vetorB[counter2 - 1:counter2 + 1])
    counter2 += 1