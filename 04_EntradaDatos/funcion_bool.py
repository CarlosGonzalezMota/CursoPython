# Programa: Función bool

# 1. Números (int y float)
print(bool(0))            # False (El vacío numérico)
print(bool(0.0))          # False
print(bool(42))           # True

# 2. Texto (Strings)
# Cadena vacía = Nada = False
print(bool(""))

# Cadena con espacio o texto = Algo = True
print(bool(" "))          # False
print(bool("Hola"))       # True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))        # False

print(bool(True))         # True
print(bool(False))        # False