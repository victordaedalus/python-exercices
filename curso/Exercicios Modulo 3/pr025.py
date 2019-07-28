"""
Todos os numeros naturais até 1000 que são multiplos de 3 e 5

"""
soma = 0
for i in range(1, 1001):
    if (i % 3) == 0 or (i % 5) == 0:
        soma += i
        print(i)

print(soma)
