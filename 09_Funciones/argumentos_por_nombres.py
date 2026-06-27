print(f'*** Función con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero, llamamos a la función pasando por los argumentos de manera posicional
imprimir_persona('Manolo', 'García', 32)

# Llamar a la función usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido='Rojas', edad=28)

# Llamar a la función argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido='Rojas', nombre='Carlos')

# Argumentos con valor por default
imprimir_persona(nombre='Carlos')