print(f'*** Promedio de Calificaciones ***')

total_calificaciones = []
numero_calificaciones = int(input('Introduce el número de calificaciones: '))

for index in range(numero_calificaciones):
    calificacion = float(input(f'Calificación[{index + 1}] = '))
    total_calificaciones.append(calificacion)

# Se realiza el cálculo del promedio de calificaciones
suma_calificaciones = sum(total_calificaciones) # 'Sum' solo aplica a valores numéricos
promedio_calificacion = suma_calificaciones / numero_calificaciones

print(f'''
    La suma total de las calificaciones es: {suma_calificaciones}
    El promedio de las calificaciones es: {promedio_calificacion:.2f}
''')