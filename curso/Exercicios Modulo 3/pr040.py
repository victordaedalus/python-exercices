"""
Inserir varios numeros e parar quando digitado numeros negativos.
e após isso falar qual foi o maior numeros, e qual foi o menor digitado.
"""
maior = 0
menor = 0

while True:
    num = int(input('Digite um numero: '))
    if num < 0:
        break

    if maior == 0:
        maior = num
    else:
        if num > maior:
            maior = num

    if menor == 0:
        menor = num
    else:
        if num < menor:
            menor = num
"""
if maior < menor:
    maior, menor
"""
print(f'Maior: {maior}, Menor: {menor}')
