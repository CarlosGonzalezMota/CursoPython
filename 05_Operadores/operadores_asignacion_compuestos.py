# Operadores de asignación compuestos

print('*** Operadores asignación compuestos ***')

a, b = 10, 15
print(f'Valor inicial: {a}, b: {b}')

# Operador compuesto de suma '+='
a += b # a = a = a + b
print(f'Operador a += b es {a}')

# Operador compuesto de resta '-='
a = 10 # Reiniciamos la variable a
a -= b # a = a - b
print(f'Operador a -= b es {a}')

# Operador compuesto de multiplicación '*='
a = 10 # Reiniciamos la variable a
a *= b # a = a * b
print(f'Operador a *= b es {a}')

# Operador compuesto de división '/='
a = 10 # Reiniciamos la variable a
a /= b # a = a / b
print(f'Operador a /= b es {a:.3f}')