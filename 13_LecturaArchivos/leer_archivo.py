print('*** Leer Archivo con Python ***')

nombre_archivo = 'mi_archivo.txt'

# Leer un archivo usando el metodo readlines
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las líneas de un archivo
    # print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# Leer el contenido del archivo usando read
print('\nLeyendo el contenido con el método read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())