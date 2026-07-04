class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonidos(self):
        print('Puedo ladrar')

    # Sobreescritura del metodo dormir
    def dormir(self):
        print('Duermo 15 horas al día')

print('*** Ejemplo de Herencia en Python ***')

print('Clase padre, soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() # Se llama el metodo sobreescrito de la clase hija
perro1.hacer_sonidos()