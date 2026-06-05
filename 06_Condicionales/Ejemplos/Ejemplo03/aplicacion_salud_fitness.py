print(f'*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

# Pedimos los valores del usuario
nombre_usuario = input('Introduce tu nombre del usuario: ')
pasos_diarios = int(input('Introduce tu pasos diarios: '))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas}')
print(f'Meta de pasos diarios alcanzados: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS}')
