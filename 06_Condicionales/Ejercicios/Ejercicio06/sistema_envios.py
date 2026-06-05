print(f'*** Sistema de Envios ***')

# Costo Tarifas
NACIONAL = 10
INTERNACIONAL = 20

# Solicitamos los valores
destino = input('Ingrese el destino (Nacional/Internacional): ')
peso_kg = float(input('Ingrese el peso del paquete en kg: '))
costo_envio = None

destino_txt = destino.strip().lower()

if destino_txt == 'nacional':
    costo_envio = peso_kg * NACIONAL
elif destino_txt == 'internacional':
    costo_envio = peso_kg * INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional')

if costo_envio is not None:
    print(f'''
        Destino: {'Nacional' if destino else 'Internacional'}
        Peso: {peso_kg}
        Coste del envio: ${costo_envio:.2f}
    ''')