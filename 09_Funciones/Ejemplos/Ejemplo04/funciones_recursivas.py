print('*** Imprimir del 1 al 5 de manera recursiva ***')

# Definir la función recursiva
def funcion_recursiva(numero):
    # Casp Base
    if numero == 1:
        print(numero, end=' ')
    else:
        print(numero, end=' ')
        funcion_recursiva(numero - 1)

# Programa principal
funcion_recursiva(5)