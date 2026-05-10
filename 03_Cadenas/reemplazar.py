# Programa: Reemplazar textos en Python

mensaje = "Hola Mundo, Mundo"

# Reemplazar TODAS las apariciones
nuevo = mensaje.replace("Mundo", "Python")
print(nuevo) # Salida: "Hola Python, Python"

# Reemplazar UNA sola vez
uno_solo = mensaje.replace("Mundo", "Dev", 1)
print(uno_solo) # Salida: "Hola Dev, Mundo"