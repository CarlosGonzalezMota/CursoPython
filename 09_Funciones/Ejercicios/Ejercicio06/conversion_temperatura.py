print('*** Convertidor de Temperatura ***')

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahreheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Ingresa la temperatura en celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F: {resultado:.2f}')

fahrenheit = float(input('Ingresa la temperatura en fahrenheit: '))
resultado = fahreheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')