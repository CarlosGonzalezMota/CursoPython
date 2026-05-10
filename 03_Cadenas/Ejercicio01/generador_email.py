print("*** Generador de Email ***\n")

# Nombre completo del usuario
nombre_completo = ' Ubaldo Acosta Soto '
print(f'Nombre usuario: {nombre_completo}')

# Nombre completo del usuario normalizado
nombre_usuario = nombre_completo.strip()
nombre_usuario_normalizado = nombre_usuario.lower().replace(' ', ".")
print(f'Nombre usuario normalizado: {nombre_usuario_normalizado}\n')

# Datos de la empresa
nombre_empresa = ' Global Mentoring '
print(f'Nombre empresa: {nombre_empresa}')
extension_dominio = '.com.mx'
print(f'Extension dominio: {extension_dominio}')

# Dominio del email normalizado
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio email normalizado: {dominio_email_normalizado}')

email = f'{nombre_usuario_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')