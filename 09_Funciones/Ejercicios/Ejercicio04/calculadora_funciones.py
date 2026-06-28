from turtledemo import __main__

print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que se pueden realizar:
    1. Suma
    2. Resta
    3. Multiplicar
    4. Dividir
    5. Salir''')

    return int(input('Ingrese su opcion: '))

def pedir_valores():
    operando1 = float(input('Ingrese el primer valor: '))
    operando2 = float(input('Ingrese el segundo valor: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()

    resultado = 0

    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado}\n')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de la división es: {resultado}\n')
    elif opcion == 5:
        print(f'Saliendo del programa de calculadora...')
        salir = True
    else:
        print('Opción invalida, escoja una opcion válida')
    return salir

if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)