"""
Teorema de Pytagoras
author: DarkBorn
"""

#Imports
from math import exp

#Execução
cateto1 = int(input('Digite o Valor do 1̣ºCateto: '))
cateto2 = int(input('Digite o Valor do 2ºCateto: '))
cateto1q = cateto1 ** 2
cateto2q = cateto2 ** 2
hipotenusa2 = cateto1q + cateto2q
hipotenusa = exp(hipotenusa2)
print('H² = {}² + {}²'.format(cateto1, cateto2))
print('H² = {} + {}'.format(cateto1q, cateto2q))
print('{} = {} + {}'.format(hipotenusa2, cateto1q, cateto2q))
print('Hipotenusa = {}'.format(hipotenusa))


