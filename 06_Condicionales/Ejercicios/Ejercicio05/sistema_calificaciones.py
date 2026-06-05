print(f'*** Sistema de calificaciones ***')

# Valores a introducir
calificacion = float(input('Introduce una calificacion (0-10): '))
calficacion_letra = None

# Hacemos la conversión del valor numérico
if 9 <= calificacion <= 10:
    calficacion_letra = 'A'
elif 8 <= calificacion < 9:
    calficacion_letra = 'B'
elif 7 <= calificacion < 8:
    calficacion_letra = 'C'
elif 6 <= calificacion < 7:
    calficacion_letra = 'D'
elif 0 <= calificacion < 6:
    calficacion_letra = 'E'
else:
    calificacion_letra = 'Valor Desconocido'

print(f'El resultado para el valor {calificacion} es una {calficacion_letra}')
