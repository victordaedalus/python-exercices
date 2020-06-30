print('Digite o salario do programador:')
salario = float(input())
print('Digite o valor de uma parcela do imprestimo:')
parcela = float(input())

if parcela > (salario / 100 * 20):
    print('Emprestimo não concedido.')
else:
    print('Emprestimo concedido.')
