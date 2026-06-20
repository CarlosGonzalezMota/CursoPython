print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': 55667711,
        'email': 'carlos@mail.com',
        'direccion': 'C/ Principal 123'
    },
    'Lucía': {
        'telefono': 99887733,
        'email': 'lucia@mail.com',
        'direccion': 'Av/ Central 456'
    },
    'Pedro': {
        'telefono': 55139078,
        'email': 'pedro@gmail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(f'{agenda}')

# Acceder a la información de un contacto específico
print(f'''Información del contacto de Lucía
    Teléfono: {agenda['Lucía']['telefono']}
    Email: {agenda['Lucía']['email']}
    Dirección: {agenda['Lucía']['direccion']}
''')

# Agregar un nuevo contacto
agenda['Aitana'] = {
    'telefono': 55678381,
    'email': 'aitana@mail.com',
    'direccion': 'C/ Salvador Díaz 321'
}

print(f'{agenda}')

# Eliminar un contacto existente
agenda.pop('Pedro')
# del agenda['Pedro']

print(f'{agenda}')

# Mostramos todos los contactos de la agenda
print(f'\nContactos de la Agenda')
for nombre, detalles in agenda.items():
    print(f'''
        Nombre: {nombre}
        Teléfono: {detalles['telefono']}
        Email: {detalles['email']}
        Direccion: {detalles['direccion']}
    ''')