# Programa: Entrada datos Python
nombre = input("Ingrese su nombre: ")
print(f"Tu nombre es: {nombre}")

# ¡CUIDADO! con la conversión de tipos al trabajar con valores numéricos
# Forma correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = int(input("Ingrese su edad: "))
print(f"Tu edad es: {edad}")
print(edad + 5) # (20 + 5 = 25)

# Para decimales (precio, altura)
altura = float(input("Ingrese su altura: "))
print(f"Tu altura es: {altura}")