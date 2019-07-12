numero = 0

for i in range(10):
    numero_local = int(input('Digite o {}º Numero: '.format(i + 1)))
    numero += numero_local

print(numero)
