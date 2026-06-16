print('*** Combinación de Listas y Tuplas ***')

# Definimos una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Pantalones', 30.00),
    ('P003', 'Sudadera', 40.00),
]

# Imprimir la información de cada producto.
# Se calcula además el precio total
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto # Unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, valor = ${precio}')
    precio_total += precio # producto[2]

print(f'Precio total de los productos: ${precio_total}')