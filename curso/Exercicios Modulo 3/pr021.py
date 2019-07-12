"""
Contador de Numeros que soma os pares da sequencia, e multiplica os impares
author: ghostborn67
"""
num1 = int(input('Digite um Numero : '))
num2 = int(input('Digite outro numero maior: '))
soma_par = 0
multi_impar = 1

for i in range(num1, num2 + 1):
    if (i % 2) == 0:
        soma_par += i

for i in range(num1, num2 + 1):
    if (i % 2) != 0:
        multi_impar *= i

print("""
Soma dos Pares {}
Multiplicação dos Impares {}
""".format(soma_par, multi_impar))
