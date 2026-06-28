print('*** Sistema de Inventarios (con funciones) ***')

# Inventario del almacén
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# Función para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f' Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    print('--- Agregar Producto ---')
    id = int(input('Ingrese el ID del producto: '))
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    nuevo_producto = {'id': id, 'nombre': nombre,
                      'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print(f'Producto agregado al inventario')

def buscar_producto_id():
    print('--- Buscar Producto ID ---')
    id_buscar = int(input('Ingrese el ID a buscar: '))
    for producto in inventario:
        if producto['id'] == id_buscar:
            print('\nInformación del producto encontrado: ')
            print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, '
                  f'Precio: ${producto.get("precio")}, Cantidad: {producto.get("cantidad")}')
            return
    print('\nProducto no encontrado')

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n---Menú---
        1. Mostrar Inventario
        2. Agregar Producto
        3. Buscar Producto por ID
        4. Salir
        ''')

        opcion = int(input('Ingrese una opción (1-4): '))

        if opcion == 1: # Mostrar inventario
            mostrar_inventario()
        elif opcion == 2: # Agregar producto
            agregar_producto()
        elif opcion == 3: # Buscar producto por id
            buscar_producto_id()
        elif opcion == 4: # Salir
            print('¡Hasta luego!')
            break
        else:
            print('Opción inválida, proporcione una opción válida')