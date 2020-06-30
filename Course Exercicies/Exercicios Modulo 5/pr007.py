"""
Função que converta graus C° em graus F°.
A formula de conversão é:

F = C * (9.0 / 5.0) + 32.0

author:VictorDaedalus
"""


def temperature_convert(celsius=0):
    farenheit = celsius * (9 / 5) + 32
    return farenheit
    

temp = float(input('Digite os C°:\n#> '))
print(f'{temperature_convert(temp)} F°')
