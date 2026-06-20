print(f'*** Playlist de Canciones ***')

# Creamos la lista vacía
lista_reproduccion = []

numero_canciones = int(input(f'Introduce un numero de canciones que desea agregar: '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for index in range(numero_canciones):
    cancion = input(f'Proporciona la cancion: {index + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabético
# lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

# Mostrar la lista iterando sus elementos
print(f'\n Iteramos la playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')