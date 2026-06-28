print('*** Regresar una tupla de valores desde una función ***')

# Definición de la función
def persona_mayusculas(nombre, apellido, edad):
   print(f'Esta función regresa varios valores (tupla)')
   return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Benítez', 18)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')