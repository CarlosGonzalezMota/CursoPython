class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre: {self.nombre}
        apellido: {self.apellido}
        Dirección memoria: {super.__str__(self)}'''

# Código principal
persona1 = Persona('Ana', 'Martínez')
print(persona1) # El metodo __str__ se llama automáticamente desde print
# print(persona1.__str__()) ESTO ES OPCIONAL