print('*** Sistema Generador de Emails ***')

nombre = input('Ingrese su nombre: ')
apellidos = input('Ingrese su apellidos: ')
nombre_empresa = input('Ingrese el nombre de la empresa: ')
extension_dominio = input('Ingrese la extensión de dominio: ')

# Normalizar los valores
nombre = nombre.strip().lower().replace(' ', '.')
apellido = apellidos.strip().lower().replace(' ', '.')
nombre_empresa = nombre_empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

# Se imprime el resultado
resultado_correo = f'{nombre}.{apellido}@{nombre_empresa}{extension_dominio}'
print(f'El resultado es: {resultado_correo}')