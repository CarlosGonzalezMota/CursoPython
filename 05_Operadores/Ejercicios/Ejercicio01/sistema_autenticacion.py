print('*** Sistema de Autenticación ***')

USUARIO = "admin"
PASSWORD = "123"

usuario_ingresado = input('¿Cuál es su usuario? ')
password_ingresado = input('¿Cuál es tu contraseña? ')

resultado = (USUARIO == usuario_ingresado.strip().lower()
             and PASSWORD == password_ingresado.strip().lower())

print(f'¿Los datos son correctos? {resultado}')