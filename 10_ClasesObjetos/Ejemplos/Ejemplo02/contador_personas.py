class Persona:

    contador_personas = 0

    def __init__(self, nombre, apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print(f'Método estático')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print(f'Método de clase')
        return cls.contador_personas

if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona***')
    persona1 = Persona('Aitana', 'Ocaña')
    persona1.mostrar_persona()

    persona2 = Persona('Ester', 'Expósito')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (class): {Persona.get_contador_personas_clase()}')