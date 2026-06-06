import random

print(f'*** Juego de Adivinanzas ***')

NUMERO_SECRETO = random.randint(1, 50)
NUMERO_INTENTOS = 0
salir = False

while not salir:
    print(f'\nNúmero de intentos: {NUMERO_INTENTOS}')
    numero = int(input('Ingrese un numero del 1 al 50: '))

    if NUMERO_INTENTOS <= 10:
        if 1 <= numero <= 50:
            if numero == NUMERO_SECRETO:
                print(f'¡Felicidades! El número secreto era: {NUMERO_SECRETO}')
                salir = True
            elif numero < NUMERO_SECRETO:
                print(f'El número secreto es mayor')
                NUMERO_INTENTOS += 1
            elif numero > NUMERO_SECRETO:
                print('El número secreto es menor')
                NUMERO_INTENTOS += 1
        else:
            print('Ingrese un numero valido')
    else:
        print(f'¡Has perdido! El número secreto era: {NUMERO_SECRETO}')