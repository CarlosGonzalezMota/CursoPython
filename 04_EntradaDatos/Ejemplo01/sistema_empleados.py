print('*** Sistema de Empleados ***')

nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe de departamento (SI/NO)? ')

# Vamos a convertir a tipo bool la variable 'es_jefe_departamento'
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del Empleado
print("\nDatos del empleado")
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Edad del empleado: {edad_empleado}")
print(f"Salario del empleado: {salario_empleado:.2f}")      # .2f --> Se indica que solo queremos 2 valores decimales y que es de tipo float
print(f"¿Es jefe de departamento? {es_jefe_departamento}")