"""
Contador de Numeros que Salva a quantidades de numeros, 
e quantas vezes esse mesmo numero apareceu.

author: ghostborn67
"""

# Variaveis
maior = 0
repeticao = 0
contador = int(input('Quantas Vezes quer ler um Numero: '))

# Execução
for i in range(contador):
    contador_local = int(input('Digite o {} Numero: '.format(i + 1)))
    if contador_local != maior:
        if contador_local > maior:
            maior = contador_local
            repeticao = 1
    elif contador_local == maior:
        repeticao += 1

print("""O Maior Numero é {}, e ele apareceu {} vezes""".format(maior, repeticao))
