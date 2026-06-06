print(f'*** Creación de Contraseña ***')

password = input('Ingresa una contraseña (debe tener al menos 6 carácteres): ')

while len(password) < 6:
    print('La contraseña no cumple con los requisitos. Debe de tener al menos 6 carácteres')
    password = input('Ingresa una nueva contraseña válida: ')
else:
    print('El valor de la contraseña es válido')