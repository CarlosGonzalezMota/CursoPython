print('*** Manejo de Tuplas ***')

# La tupla (tuple) es similar a una colección, con la diferencia de que estas son inmutables (no se pueden modificar)
mi_tupla = (1,2,3,4,5)
print(mi_tupla) # Otra diferencia, es que se imprime con 'paréntesis', en vez de 'corchetes'

# Iteramos los elementos de una tupla:
for index in mi_tupla:
    print(index, end=' ')

# Crear una tuple para una coordenada 'x','y'
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de 1 solo elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidadas = (1, (2, 3), (4, 5))
print(f'Listado de tuplas anidadas: {tuplas_anidadas}')