print(f'*** Bienvenidos a la Casa de los Espejos ***')

edad = int(input('Ingrese su edad: '))
tienes_miedo_oscuridad = input('¿Tienes miedo a la oscuridad? (Si/No) ')
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print(f'Puedes entrar a la casa de los espejos')
else:
    print(f'Lo siento, la Casa de los Espejos podría darte miedo')