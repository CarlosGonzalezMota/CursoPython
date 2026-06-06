print(f'*** Función Range en Python ***')

print('Secuencia del 0 al 4')
# inicio = 0 (Opcional)
# fin = 5 - 1 = 4
# incremento = 1 (Opcional)
for i in range(5): # fin = 5
    print(i, end=' ')

print(f'\n\nSecuencia del 1 al 10')
for i in range(10, 20 + 1):
    print(i, end=' ')

print(f'\n\nSecuencia del 20 al 30 de 2 en 2')
for i in range(20, 30 + 1, 2):
    print(i, end=' ')