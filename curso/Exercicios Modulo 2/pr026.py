print('Digite a Quantidade de kilometros percorridos:')
km = float(input())
print('Quantos os litros de gasolina consumidos:')
l = float(input())

km_l = km / l

if km_l < 8:
    print('Venda o Carro!')
elif 8 > km_l > 12:
    print('Economico!!')
else:
    print('MUITO ECONOMICO!!!!!!!!!!!!')
