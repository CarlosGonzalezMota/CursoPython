print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es 0')
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as excepcion:
        print(f'Ocurrió un error: {excepcion}')
    else:
        print(f'No ocurió ningún error')
    finally:
        print(f'Se terminó de procesar la excepción\n')
    # except ZeroDivisionError:
    #    print('Error: No se puede dividir por 0')
    # except TypeError:
    #    print('Error: Los operandos deben ser numéricos')

# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')