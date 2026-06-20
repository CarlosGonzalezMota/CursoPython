print('*** Lista de Suscriptores ***')

# Definir el set inicial
suscriptores = set()

numero_suscriptores = int(input('Introduce un numero de suscriptores: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

# Verificar si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Proprociona el nuevo suscriptor: ')

if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')

print(f'Lista de suscriptores actualizada: {suscriptores}')

# Eliminar un suscriptor ya existente
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado correctamente')

print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de suscriptores ---')
for suscriptor in suscriptores:
    print(f' - {suscriptor}')