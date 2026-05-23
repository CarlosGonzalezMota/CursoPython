print('*** Operador lógico not ***')

condicion1 = False
resultado = not condicion1
print(f'Operador not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'\n¿La variable no tiene ningún valor? {es_cadena_vacia}')

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\n¿La variable no tiene ningún valor asignado? {es_variable_sin_valor}')