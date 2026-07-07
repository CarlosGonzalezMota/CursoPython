# Definición de una clase
class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dirección de memoria self: {id(self)}')
        print(f'Dirección de memoria self hexadecimal: {hex(id(self))}')  # Al llamar a "mostrar_persona", es lo que el param self lee

# Creación de Objetos
if __name__ == '__main__':
    # Creación de un primer objeto
    persona1 = Persona('Layla', 'Ortega') # Crea un objeto vacío en memoria
    persona1.mostrar_persona()

    # Creación de un segundo objeto
    persona2 = Persona('Rick', 'Sánchez')
    persona2.mostrar_persona()