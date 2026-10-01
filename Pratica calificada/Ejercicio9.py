class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def a_formato_texto(self) -> str:
        return f"{self.titulo},{self.autor},{self.paginas}"


def guardar_libros(libros: list, archivo_salida: str = "libros.txt"):
    try:
        with open(archivo_salida, "w", encoding="utf-8") as f:
            for libro in libros:
                f.write(libro.a_formato_texto() + "\n")
        print(f"Se guardaron con exito {len(libros)} libros en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al guardar los libros: {e}")


def main():
    coleccion = [
        Libro("Rayuela", "Julio Cortazar", 600),
        Libro("Ficciones", "Jorge Luis Borges", 224),
        Libro("Los Rios Profundos", "Jose Maria Arguedas", 288),
        Libro("Conversacion en La Catedral", "Mario Vargas Llosa", 736)
    ]

    guardar_libros(coleccion)


if __name__ == "__main__":
    main()