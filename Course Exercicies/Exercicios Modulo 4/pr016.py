"""
Criar um programa que pega 5 valores e após isso solicita um codigo.
Se o codigo for 1, o mesmo mostra o vetor na posição inicial,
Se for 2, o mesmo mostra o vetor na posição inversa,
Se for outro numero, mostra a mensagem de erro e pede para digitar o codigo denovo.

author:ghostborn67 
"""

lista = []

for x in range(5):
    lista.append(int(input(f'Digite o {x + 1}° numero: ')))

print('Digite a opção desejada:')
option = int(input('$> '))

while True:
    if option == 1:
        print(lista)
        break
    elif option == 2:
        lista.reverse()
        print(lista)
        break
    else:
        print('Opção Incorreta, Digite Novamente')
        option = int(input('$> '))
