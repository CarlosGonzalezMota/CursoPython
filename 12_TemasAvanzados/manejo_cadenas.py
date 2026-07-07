# Dividir una cadena split() --> (parsing)
cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

# Buscar con find()
posicion = cadena.find('Mundo') # Devuelve el valor de 5
print(f'Posición de la cadena mundo: {posicion}')

# Reemplazar con replace()
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplación de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 3
print(f'Resultado de la multiplicación de cadenas: {resultado_multiplicacion_cadenas}')