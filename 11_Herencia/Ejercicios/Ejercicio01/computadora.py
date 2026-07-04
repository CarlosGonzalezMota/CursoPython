from Ejercicio01.monitor import Monitor
from Ejercicio01.raton import Raton
from Ejercicio01.teclado import Teclado

class Computadora():
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadoras = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self._id_computadoras}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('Asus', 27)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('Razer', 'Bluetooth')
    raton2 = Raton('Razer', 'Bluetooth')
    monitor2 = Monitor('Dell', 34)
    computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
    print(computadora2)