print('*** Máquina de Snacks ***')

snacks = [
    {'id': 1, 'nombre': 'Salchipapas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacía). Son los snacks ya comprados
productos = []

def mostrar_snacks():
    print('--- Snacks disponibles ---')
    for snack in snacks:
        print(f'\tId: snack {snack['id']} -> {snack['nombre']} '
              f'- ${snack['precio']}')

def buscar_snack_id(id_snack):
    for snack in snacks:
        if snack['id'] == id_snack:
            return snack
    return None

def comprar_snacks():
    id_snack = int(input('¿Qué snack desea comprar? (id): '))
    snack_encontrado = buscar_snack_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack no encontrado con ID: {id_snack}')

def mostrar_ticket():
    ticket = f'\t---Ticket de venta---'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto['id']} -> {producto['nombre']} - ${producto['precio']}'
        total += producto['precio']
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

if __name__ == '__main__':
    while True:
        print(f'''Menú:
        1. Mostrar snacks
        2. Comprar snacks
        3. Mostrar ticket
        4. Salir
        ''')

        opcion = int(input('Ingrese su opción: '))

        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('¡Hasta luego!')
            break
        else:
            print('Opción invalida! Por favor, escoja una opción válida.')