print(f'*** Estación del año ***')

# Se proporciona la fecha entre 1 y 12
valor_mes = int(input('Ingresa el valor del mes (1 al 12): '))
estacion = None

if valor_mes == 1 or valor_mes == 2 or valor_mes == 12:
    estacion = 'Invierno'
elif valor_mes == 2 or valor_mes == 4 or valor_mes == 5:
    estacion = 'Primavera'
elif valor_mes == 6 or valor_mes == 7 or valor_mes == 8:
    estacion = 'Verano'
elif valor_mes == 9 or valor_mes == 10 or valor_mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación Desconocida'

print(f'La estación para el {valor_mes} es: {estacion}')