print('Quantos dias o encanador trabalhou:')
days = int(input()) 
pre_sal = 30.0
final_sal = (days * pre_sal) - (days * pre_sal / 100 * 8)
print('O encanador ganhou R${}'.format(final_sal))


