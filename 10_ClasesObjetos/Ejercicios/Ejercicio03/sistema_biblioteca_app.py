from Ejercicios.Ejercicio03.biblioteca import Biblioteca
from Ejercicios.Ejercicio03.libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {bibliotecaNacional.nombre} ***')

# Definición de libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3 = Libro('El Amor en los tiempo de Cólera', 'Gabriel García Márquez', 'Ficción')
libro4 = Libro('Pedro Páramo', 'Juan Rulfo', 'Ficción')
libro5 = Libro('Pantaleón y las visitadoras', 'Mario Vargas Llosa', 'Comedia')

# Agregar los libros a la bibloteca
bibliotecaNacional.libros.append(libro1)
bibliotecaNacional.libros.append(libro2)
bibliotecaNacional.libros.append(libro3)
bibliotecaNacional.libros.append(libro4)
bibliotecaNacional.libros.append(libro5)

# Buscar libros por autor
autor = 'Gabriel García Márquez'
print(f'\nLibros de autor: {autor}')
bibliotecaNacional.bucar_libros_por_autor(autor)

# Buscar libros por género
genero = 'Ficción'
print(f'\nLibros de genero: {genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros de la biblioteca
bibliotecaNacional.mostrar_todos_los_libros()