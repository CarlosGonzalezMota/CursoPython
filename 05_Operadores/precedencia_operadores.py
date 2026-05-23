# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

# Ejemplo de precedencia de operadores
resultado = 12 / 3 + 2 * 3 -1
# 1. División 12 / 3  = 4
# 2. Multiplicación 2 * 3 = 6
# 3. Suma 4 + 6 = 10
# 4. Resta 10 - 1 = 9
print(f'Resultado: {resultado:.2f}')