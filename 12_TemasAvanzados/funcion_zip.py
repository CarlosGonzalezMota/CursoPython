nombre = ['Juan', 'Maria', 'Pedro', 'Ana']
edades = [30, 25, 35]
ciudad = ['Madrid', 'Barcelona', 'Sevilla']

# Combinar los elementos correspondientes usando la función zip
personas = zip(nombre, edades, ciudad)

# Iterar sobre el resultado de la función zip
for persona in personas:
    print(persona)  # Se compone de una tupla