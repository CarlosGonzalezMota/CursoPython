print('*** Decoradores en Python ***')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función de saludar')
        resultado = funcion(*args, **kwargs)
        print('Después de llamar a la función de saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')