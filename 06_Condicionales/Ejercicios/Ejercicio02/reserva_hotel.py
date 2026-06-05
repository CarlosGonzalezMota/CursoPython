print(f'*** Sistema de Reserva de Hotel ***')

# Tarifas del hotel
TARIFA_SIN_VISTA_MAR = 150.50
TARIFA_CON_VISTA_MAR = 190.50

# Información del usuario
nombre_cliente = input('Nombre del cliente: ')
dias_estancia = int(input('Dias de estancia: '))
vista_mar_txt = input('¿La habitación tiene vistas al mar? (Si/No) ')

vista_mar = vista_mar_txt.strip().lower() == 'si'

if vista_mar:
    coste_total = TARIFA_CON_VISTA_MAR * dias_estancia
else:
    coste_total = TARIFA_SIN_VISTA_MAR * dias_estancia

print(f'''
    ----------------Detalles de la Reserva----------------
    Cliente: {nombre_cliente}
    Días de estáncia: {dias_estancia}
    Coste total: ${coste_total:.2f}
    Habitación con vista al mar: {'Si' if vista_mar else 'No'}'
''')