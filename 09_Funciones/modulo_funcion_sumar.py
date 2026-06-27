# Definimos la función
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

# Prueba de la función sumar
if __name__ == '__main__': # Con esto, le decimos a Python que solo se ejecute la función si se lanza desde este archivo
    print(f'Prueba desde el módulo sumar {sumar(15, 35)}')