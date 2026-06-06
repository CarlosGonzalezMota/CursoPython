print(f'*** Aplicación Cajero Automático ***')

SALDO = 1000
salir = False

while not salir:
    print(f'''
    Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir
    ''')

    opcion = float(input('Escoje una opcion: '))

    if opcion == 1:

        print(f'Su saldo actual es de: ${SALDO:.2f}')
    elif opcion == 2:
        saldo_retirar = float(input('Ingresa al cantidad que desea retirar: '))
        if saldo_retirar <= SALDO:
            SALDO = SALDO - saldo_retirar
            print(f'Su saldo actual es de: ${SALDO:.2f}')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual ${SALDO:.2f}')
    elif opcion == 3:
        saldo_ingresar = float(input('Ingresa al cantidad de ingresar: '))
        SALDO = SALDO + saldo_ingresar
        print(f'Su nuevo saldo es de ${SALDO:.2f}')
    elif opcion == 4:
        print('Saliendo del cajero automático. Hasta pronto!')
        salir = True
    else:
        print('Opcion invalida, por favor ingrese una opcion valida')

