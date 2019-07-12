num = int(input('Digite Um Numero entre 100 e 999: '))
if 100 <= num <= 999:
    for i in str(num):
        print(i)
else:
    print('O Numero que digitou está errado')
