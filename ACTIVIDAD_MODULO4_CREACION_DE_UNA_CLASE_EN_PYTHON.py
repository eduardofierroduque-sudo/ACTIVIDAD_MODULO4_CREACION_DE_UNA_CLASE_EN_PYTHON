# 1. Creación de la Clase Principal: Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Atributos inicializados mediante el constructor
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas

    # Métodos Accesores (Getters)
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_paginas(self):
        return self._paginas

    # Métodos Mutadores (Setters)
    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self._autor = nuevo_autor

    def set_paginas(self, nuevas_paginas):
        self._paginas = nuevas_paginas


# 2. Relación de Colaboración: Biblioteca
class Biblioteca:
    def __init__(self):
        # Atributo libros: una lista vacía para almacenar objetos Libro
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado a la Biblioteca.")

    def mostrar_libros(self):
        print("\n--- Libros en la Biblioteca ---")
        for libro in self.libros:
            print(f"Título: {libro.get_titulo()} | Autor: {libro.get_autor()}")


# 3. Relación de Composición: Estante
class Estante:
    def __init__(self):
        # Atributo libros: lista de objetos Libro
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' colocado en el Estante.")

    def mostrar_libros(self):
        print("\n--- Libros en el Estante ---")
        for libro in self.libros:
            print(f"Título: {libro.get_titulo()} | Autor: {libro.get_autor()}")


# 4. Prueba el Código
if __name__ == "__main__":
    # Crear al menos dos objetos de la clase Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1000)
    libro4 = Libro("Rayuela", "Julio Cortázar", 600)
    libro5 = Libro("La desaparición", "Georges Perec", 312)
    libro6 = Libro("Los detectives salvajes", "Roberto Bolaño", 616)
    libro7 = Libro("El Aleph", "Jorge Luis Borges", 146)
    libro8 = Libro("Ficciones", "Jorge Luis Borges", 224)
    libro9 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 368)
    libro10 = Libro("La sombra del viento", "Carlos Ruiz Zafón", 576)   
    libro11 = Libro("El nombre de la rosa", "Umberto Eco", 512)
    libro12 = Libro("La ciudad y los perros", "Mario Vargas Llosa", 448)
    

    # Crear objeto de la clase Biblioteca y agregar libros
    mi_biblioteca = Biblioteca()
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)
    mi_biblioteca.agregar_libro(libro5)
    mi_biblioteca.agregar_libro(libro6)
    mi_biblioteca.agregar_libro(libro7)
    mi_biblioteca.agregar_libro(libro8)
    mi_biblioteca.agregar_libro(libro9)
    mi_biblioteca.agregar_libro(libro10)
    mi_biblioteca.agregar_libro(libro11)
    mi_biblioteca.agregar_libro(libro12)
    

    # Crear objeto de la clase Estante y agregar libros
    mi_estante = Estante()
    mi_estante.agregar_libro(libro1)
    mi_estante.agregar_libro(libro2)
    mi_estante.agregar_libro(libro3)
    mi_estante.agregar_libro(libro4)
    mi_estante.agregar_libro(libro5)
    mi_estante.agregar_libro(libro6)
    mi_estante.agregar_libro(libro7)
    mi_estante.agregar_libro(libro8)
    mi_estante.agregar_libro(libro9)
    mi_estante.agregar_libro(libro10)
    mi_estante.agregar_libro(libro11)
    mi_estante.agregar_libro(libro12)


    # Verificar funcionalidad llamando a mostrar_libros()
    mi_biblioteca.mostrar_libros()
    mi_estante.mostrar_libros()
 