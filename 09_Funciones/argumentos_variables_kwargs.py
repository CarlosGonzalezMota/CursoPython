# *args - arguments - tupla
# **kwargs - keyword arguments (key, value) como un dict
print('*** Argumenos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos a la función
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armadura', 'Playboy', edad=45)

# Es opcional mandar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buen pana')