# Operadores asignación

print('*** Operadores de asignación ***')

numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero modificado: {numero}')

cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignación múltiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignación encadenada
a = b = c = 0
print(f'Valor de a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10 # Aplicando el concepto de asignación múltiple, se intercambian valores
print(f'Valor original de x = {x}, y = {y}')
x, y = y, x
print(f'Invertir los valores de x = {x}, y = {y}')

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input('Ingrese tu nombre y apellidos separados por comas: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')