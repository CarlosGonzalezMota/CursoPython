print('*** Sistema de Inventarios ***')

inventario = []

numero_productos = int(input('¿Cuántos productos desea agregar al inventar? '))

for index in range(numero_productos):
    print(f'Proporcione los valores del producto {index+1}')
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad de productos: '))
    # Creamos el diccionario con el detalle del producto
    producto = {'id': index+1, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostramos el inventario inicial
print(f'\nInventario inicial: {inventario}')

# Buscar un producto por id
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto['id'] == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'Información del producto encontrado: ')
    print(f'''
        ID: {producto_encontrado['id']}
        Nombre: {producto_encontrado['nombre']}
        Precio: {producto_encontrado['precio']}
    ''')
else:
    print(f'No existe el producto con ID: {id_buscar}')

# Mostramos el inventario detallado
print(f'\n--- Inventario detallado ---')
for producto in inventario:
    print(f'''
        ID: {producto['id']}
        Producto: {producto['nombre']}
        Precio: {producto['precio']}
    ''')