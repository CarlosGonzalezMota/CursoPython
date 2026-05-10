# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Básico [inicio:fin]
print(texto[0:4]) # "PROG" (El índice 4 no se incluye)

# 2. Atajo desde el inicio [:fin]
print(texto[:4]) # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [inicio:]
print(texto[8:]) # "CION" (Hasta el último char)

# 4. Índices negativos
print(texto[-4:]) # "CION" (Los últimos 4)

# 5. Pasos [::paso] # (Invertir cadena)
print(texto[::-1]) # NOICAMARGORP"
print(texto[::-2]) # NIAAGR" (Recupera los valores invertidos cada 2 posiciones
print(texto[::2]) # NIAAGR" (Recupera los valores cada 2 posiciones
