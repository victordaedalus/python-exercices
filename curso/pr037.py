print('Digite o valor do produto:')
valor = float(input())
valor_final = valor - (valor / 100 * 12)
print('O produto com 12% de desconto é de {}'.format(valor_final))
