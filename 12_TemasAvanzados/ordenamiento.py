print(f'*** Ordenamiento en Python ***')

# sintaxis = sorted(iterable, key=None, reverse=False)
empleados = ['Juan', 'Pedro', 'Maria']
# Ordenar la lista
empleados_ordenados = sorted(empleados)
# empleados_ordenados = sorted(empleados, reverse=True)
print(f'Empleados ordenados: {empleados_ordenados}')

# Ordenar un diccionario (una llave)
empleados_dict = [
    {'nombre': 'Juan', 'salario': 3000},
    {'nombre': 'María', 'salario': 2500},
    {'nombre': 'Pedro', 'salario': 3500},
]
empleados_dict_ordenados = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'Empleados ordenados por salario: {empleados_dict_ordenados}')