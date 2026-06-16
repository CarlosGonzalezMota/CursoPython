print('*** Desempaquetado de Tuplas ***') # Unpacking

producto = ('P001', 'Camiseta', 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes desempaquetados
print(f'Producto: id = {id}, Descripcion = {descripcion}, Precio = {precio}')