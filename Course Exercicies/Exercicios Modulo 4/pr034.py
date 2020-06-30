"""
Criar um vetor que receba 10 numeros diferentes, e que toda vez em que o numero digitado já existe na lista,
é dado a mensagem de erro e pede para digitar outro numero.

author:ghostborn67
"""

vetor = []

for i in range(10):
    nun = int(input(f'Digite {i + 1}° Numero: '))
    if nun in vetor:
        while True:
            print('Numero já existente!')
            nun2 = int(input(f'Digite {i + 1}° Numero: '))
            if nun != nun2:
                vetor.append(nun2)
                break
    else:
        vetor.append(nun)

print(vetor)
