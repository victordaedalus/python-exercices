print('Qual é o salario base: ')
base = float(input()) 
final = base + (base / 100 * 5) - (base * 100 / 7) 
print('O salario final do empregado é de R${}'.format(final))
