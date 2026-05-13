print('*** Receta de Cocina ***')

nombre_receta = input('Ingrese el nombre: ')
ingredientes_receta = input('Ingrese los ingredientes: ')
tiempo_preparacion = int(input('Ingrese el tiempo de preparación (min): '))
dificultad_preparacion = str(input('Ingrese la dificultad: '))

print("-" * 30)

print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes de la receta: {ingredientes_receta}")
print(f"Tiempo de preparacion: {tiempo_preparacion}")
print(f"Dificultad de la preparacion: {dificultad_preparacion}")