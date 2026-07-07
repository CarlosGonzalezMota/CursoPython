print('*** Función de Sum y Next ***')

lista = [1,2,3,4,5]

# Suma de todos los elementos
resultado = sum(lista)
print(f'Resultado de sum: {resultado}')

# Podemos proporcionar un valor inicial
resultado = sum(lista, 20)
print(f'Resultado de sum con valor inicial de 20: {resultado}')

# Función de Next
iterador = iter(lista) # Se convierte en una lista iterada

# Obtener el próximo elemento del iterador
print(f'Resultado de next: {next(iterador)}')
print(f'Resultado de next: {next(iterador)}')