"""
Mostrar varios numeros com a r², r³, sqrt
"""
from math import sqrt
while True:
    num = int(input('Digite o numero: '))
    if num <= 0:
        break
    print(f'''
    
    num = {num}
    num² = {num ** 2}
    num³ = {num ** 3}
    raiz(num) = {sqrt(num)}
    
    ''')
