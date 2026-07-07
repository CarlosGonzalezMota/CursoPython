from functools import reduce

print('*** Funciones lambnda ***')

# Función cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de 5: {cuadrado(5)}')

# Función lambda (anónima)
cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 2: {cuadrado_lambda(2)}')

# Con map y lambda, creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar una función lambda para obtener el cuadrado de cada número
cuadrados = list(map(lambda x: x ** 2, numeros)) # Por cada elemento, se aplica el lambda
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de los números pares: {pares}')

# Reduce y map
suma_iterativa = reduce(lambda x, y: x + y, numeros)
print(f'Resultado de suma iterativa: {suma_iterativa}')