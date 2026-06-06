print(f'*** Aplicación Calculadora ***')

salir = False
operando1 = operando2 = resultado = 0

while not salir:
    print(f'''
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Salir
    ''')

    opcion = int(input('Escoje una opcion: '))

    if 1 <= opcion <= 4:
        operando1 = float(input('Escoja el primer valor: '))
        operando2 = float(input('Escoja el segundo valor: '))

    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado:.2f}')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de la division es: {resultado:.2f}')
    elif opcion == 5:
        print(f'Saliendo de la calculadora. Hasta pronto!')
        salir = True
    else:
        print('Opción invalida. Por favor, escoja una opción válida')