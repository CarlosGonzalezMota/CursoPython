# Programa: Regsitro de explorador espacial

# Asignar valores a las variables
nombre_explorador = "Luna Vega"
planeta_origen = 'Marte'
edad_explorador = 29
misiones_completadas = 4
nivel_energia = 87.5

# for = 15 --> Esto arroja un error, ya que 'for' es una palabra reservada por python

Nivel_Energia = 90.5 # No es una buena práctica
NIVEL_ENERGIA = 100.0 # Se considera que es una constante
nivel_energía = 80.0 # No se deben utilizar caracteres especiales (acentos, ñ...)

# Imprimir los valores
print("=== REGISTRO ESPACIAL ===")
print(nombre_explorador, planeta_origen, edad_explorador, misiones_completadas, nivel_energía, Nivel_Energia, NIVEL_ENERGIA, nivel_energia)