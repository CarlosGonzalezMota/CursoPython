class Animal:
    def hacer_sonidos(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonidos(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonidos(self):
        print('Puedo maullar')

# Función polimorfica
def hacer_sonidos_animal(animal):   # Duck typing
    animal.hacer_sonidos()

print('*** Ejemplo de Polimorfismo ***')

print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonidos_animal(animal1)

print('\nClase Hija Perro: ')
perro1 = Perro()
hacer_sonidos_animal(perro1)

print('\nClase Hija Gato: ')
gato1 = Gato()
hacer_sonidos_animal(gato1)