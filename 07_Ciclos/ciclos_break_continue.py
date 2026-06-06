print(f'*** Break y Continue ***')

# Ejemplo con break
for numero in range(1, 10):
    if numero % 2 == 0:
        print(f'Número par {numero}')
        break # Salimos del ciclo inmediatamente

print()

# Ejemplo con continue
for numero in range(1, 10):
    if numero % 2 == 1:
        continue
    print(numero)