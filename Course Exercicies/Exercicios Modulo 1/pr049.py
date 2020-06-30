"""
Experimento Errado...
Codigo não funcional.......

"""

# Entradas
print('Digite o horario de inicio:')
segundos = int(input('Segundos: '))
minutos = int(input('Minutos:'))
horas = int(input('Horas: '))
print('Quanto tempo vai durar o experimento?', 20 * '\n')
segundos_final = int(input('Segundos: '))
minutos_final = int(input('Minutos:'))
horas_final = int(input('Horas: '))

# Processo
segundos_processo = segundos + segundos_final
minutos_processo = minutos + minutos_final
horas_processo = horas + horas_final

if segundos_processo >= 60:
    minutos_processo = minutos_processo + (segundos_processo / 60)
    segundos_final = segundos_processo % 60

if minutos_processo >= 60:
    horas_processo = horas_processo + (minutos_processo / 60)
    minutos_final = minutos_processo % 60

if horas_processo >= 24:
    horas_final = 24 - horas_processo

# Saida
print("""
O experimento irá terminar a:
{} Segundos
{} Minutos
{} Horas
""".format(segundos_final, minutos_final, horas_final))
