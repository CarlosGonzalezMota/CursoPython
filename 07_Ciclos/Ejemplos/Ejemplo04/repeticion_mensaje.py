print(f'*** Repetición de un Mensaje ***')

mensaje = input('Ingrese mensaje a repetir: ')
numero_de_repeticiones = int(input('Ingrese un número de repeticiones: '))

# Iterar sobre el rango de repeticiones
for i in range(numero_de_repeticiones):
    print(f'{i} - {mensaje}')
# En caso de no querer utilizarse el 'índice', se puede definir con '_'
for _ in range(numero_de_repeticiones):
    print({mensaje})