class ClaseAritmetica:
    # Para poder pasar los valores de manera opcional, se declara el valor NONE
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        return print(f'Resultado de la suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        return print(f'Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        return print(f'Resultado de la multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        return print(f'Resultado de la división: {resultado:.2f}')

if __name__ == '__main__':
    print('*** Ejemplo clase Aritmética ***')
    # Primer Objeto
    artimetica1 = ClaseAritmetica(5, 7)
    artimetica1.sumar()
    artimetica1.restar()
    print()
    # Segundo Objeto
    artimetica2 = ClaseAritmetica(12, 16)
    artimetica2.multiplicar()
    artimetica2.dividir()
    print()
    # Tercer Objeto
    artimetica3 = ClaseAritmetica(7)
    artimetica3.operando2 = 9
    artimetica3.sumar()
    print()
    # Cuarto Objeto
    artimetica4 = ClaseAritmetica()
    artimetica4.operando1 = 10
    artimetica4.operando2 = 8
    artimetica4.sumar()
    print()
    # Quinto Objeto
    artimetica5 = ClaseAritmetica(operando1=3, operando2=1)
    artimetica5.dividir()