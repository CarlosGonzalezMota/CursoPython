from Ejercicio01.computadora import Computadora
from Ejercicio01.monitor import Monitor
from Ejercicio01.orden import Orden
from Ejercicio01.raton import Raton
from Ejercicio01.teclado import Teclado

print('*** Mundo PC ***')

# Computadora 1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Asus', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

# Computadora 2
teclado2 = Teclado('Razer', 'Bluetooth')
raton2 = Raton('Razer', 'Bluetooth')
monitor2 = Monitor('Dell', 34)
computadora2 = Computadora('Dell', monitor2, teclado2, raton2)

# Crear lista de computadoras
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Asus', 31)
computadora3 = Computadora('Asus', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)