sec = int(input('Digite quantos segundos:\n> '))
minutos = sec / 60
horas = minutos / 60
print("""
{} Segundos
{} Minutos
{} Horas
""".format(int(sec), int(minutos), int(horas)))
