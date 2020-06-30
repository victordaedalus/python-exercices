"""
Contagem regressiva
author: Ghostborn67
"""
from time import sleep


counter = int(input('Digite quantos segundos vai ter a contagem: '))
for _ in range(counter):
    print(counter)
    sleep(1)
    counter -= 1
print('FIM!!"')
