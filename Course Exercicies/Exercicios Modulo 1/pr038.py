print('Qual é o valor do salario base:')
base = float(input())
upgrade = base + (base / 100 * 25)
print('O salario do aumento é de R${}'.format(upgrade))
