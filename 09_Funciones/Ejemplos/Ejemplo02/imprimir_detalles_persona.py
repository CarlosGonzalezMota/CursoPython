print('*** Imprimir detalles de una Persona usando kwargs ***')

# Función que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# Llamamos a la función
imprimir_detalle_persona(nombre='Carla', edad=30, ciudad='Buenos Aires')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Bogotá', puesto='Ingeniero')