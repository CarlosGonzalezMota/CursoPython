print(f'*** Sumas Iterativas ***')

# Sumar los 5 primeros números
MAXIMO = 50
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada -> {acumulador_suma}\n')

print(f'\nResultado de la suma acumulada: {acumulador_suma}')