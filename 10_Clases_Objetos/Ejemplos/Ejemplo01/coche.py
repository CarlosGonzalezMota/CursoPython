class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    @property # Definir el metodo GET de manera más pythonica
    def marca(self):
        return self._marca

    @marca.setter # Definir el metodo SET de manera mas pythonica
    def marca(self, marca):
       self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

# Programa principal
if __name__ == '__main__':
    # Creación del primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberíamos de acceder a los atributos que no sean públicos
    print()
    # Atributo de marca del coche 1
    print(f'Atributo marca coche1: {coche1.marca}')
    coche1.marca = 'Toyota2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Verde'
    # Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valon nuevo atributo')
    coche1.conducir()
    print(coche1.nuevo_atributo)