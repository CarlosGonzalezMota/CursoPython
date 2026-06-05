print(f'*** Sistema de envios ***')

# Valores admin
USUARIO_ADMIN = "admin"
CONTRASENIA_ADMIN = "admin"

# Valores del usuario
valor_usuario = input('Introduzca un Usuario: ')
valor_contrasenia = input('Introduzca la contrasenia: ')

if valor_usuario == USUARIO_ADMIN and valor_contrasenia == CONTRASENIA_ADMIN:
    print('Bienvenido al Sistema')
elif valor_usuario != USUARIO_ADMIN and valor_contrasenia == CONTRASENIA_ADMIN:
    print('Usuario inválido')
elif valor_usuario == USUARIO_ADMIN and valor_contrasenia != CONTRASENIA_ADMIN:
    print('Contraseña inválida')
elif valor_usuario != USUARIO_ADMIN and valor_contrasenia != CONTRASENIA_ADMIN:
    print('Usuario y Contraseña inválidos')

