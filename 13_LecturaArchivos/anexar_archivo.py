print('*** Anexar información Archivo ***')

nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    # Anexar información al archivo
    archivo.write('Anexando informacion...\n')
    archivo.write('Saliendo de anexar informacion')

print(f'Se ha anexado informacion al archivo {nombre_archivo}')