print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unir 2 set
union = a | b
print(f'Unión a | b: {union}')

# Interseccion
interseccion = a & b
print(f'Intersección a & b {interseccion}')

# Diferencia
diferencia = a - b
print(f'Diferencia a - b {diferencia}')