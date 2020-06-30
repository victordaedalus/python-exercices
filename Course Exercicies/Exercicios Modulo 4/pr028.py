"""
Criar vetor que armazene 10 numeros inteiros e após isso criar um vetor1 que armazene todos os numeros impares e o
vetor2 que armazene todos os pares, e ao final mostrar o elementos que foram usados em ambos.
author:ghostborn67
"""


def par(number):
    if number % 2 == 0:
        return True
    else:
        return False


vetor = []
vetor1 = []
vetor2 = []

for x in range(10):
    vetor.append(int(input(f'Digite o {x + 1}° numero : ')))

for item in vetor:
    if par(item) is True:
        vetor2.append(item)
    else:
        vetor1.append(item)

print(f"""
Os Numeros Usados no vetor1 forão:
{vetor1}

Os Numeros Usados no vetor2 forão:
{vetor2}
""")
