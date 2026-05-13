from random import randint

print('*** Sistema Generador ID Único ***')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
anio_nacimiento = input('Ingrese su año de nacimiento (YYYY): ')

# Normalizar los valores
resultado_nombre = nombre.strip().upper()[0:2]
resultado_apellido = apellido.strip().upper()[0:2]
resultado_anio_nacimiento = anio_nacimiento.strip()[-2:]

resultado_datos = f'{resultado_nombre}{resultado_apellido}{resultado_anio_nacimiento}'

# Se genera el ID random y se muestra el resultado entero
id_unico = randint(1000, 9999)

print(f''''\nHola {nombre}
    Tu nuevo número de identificación (ID generado por el sistema es:
    {resultado_datos}{id_unico}
    ¡FELICIDADES!
''')
