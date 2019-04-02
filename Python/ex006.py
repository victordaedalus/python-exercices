from random import randint
from time import sleep
     
     
def linha(txt):
    line = len(txt) + 4
    print('-=' * int(line - line // 2))
    print(f'  {txt}')
    print('-=' * int(line - line // 2))
     
     
linha('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    try:
        while True:
            palpite_user = int(input('Coloque um número: '))
            if palpite_user > 10:
                print('\033[31mERRO! Digite apenas números menores que 10.\033[m')
            else:
                break
    except ValueError:
        print(f'\033[31mValueError\033[m!, O valor digitado foi rejeitado, trocaremos por 0 (padrão)')
        palpite_user = 0
        break
    break
computer = randint(0, 10)
par_ou_impar = computer + palpite_user

while True:
    par_impar_user = str(input('Par ou Ímpar [P/I]: '))[0].upper()
    if par_impar_user not in 'PI':
        print('\033[31mDigite apenas P para Par ou I para Ímpar.\033[m')
    else:
        break

print('\033[36mGERANDO RESULTADOS..\033[m')

sleep(1.5)

if par_ou_impar % 2 == 0:
    resultado = 'PAR'
else:
    resultado = 'ÍMPAR'
print('-' * 85)

print(f'Você jogou {palpite_user} e o computador {computer}. Totalizando {par_ou_impar}. {par_ou_impar} é '
        f'igual a {resultado}, então..', end=' ')

if resultado[0] == par_impar_user:
    print('\033[34mVOCÊ GANHOU!\033[m')
else:
    print('\033[31mVOCÊ PERDEU!\033[m')
print('-' * 85)