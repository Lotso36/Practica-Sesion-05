import csv

class Libro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.numero_paginas} pags.)"


def main():
    libros = [
        Libro("Cien Anios de Soledad", "Gabriel Garcia Marquez", 471),
        Libro("El Tunel", "Ernesto Sabato", 160),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863),
        Libro("La Ciudad y los Perros", "Mario Vargas Llosa", 448)
    ]

    print("=== LISTA DE LIBROS EN CONSOLA ===")
    for libro in libros:
        print(f" - {libro}")

    archivo_csv = "libros.csv"
    try:
        with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Titulo", "Autor", "Numero de Paginas"])
            for l in libros:
                escritor.writerow([l.titulo, l.autor, l.numero_paginas])

        print(f"\nDatos exportados exitosamente a '{archivo_csv}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo CSV: {e}")


if __name__ == "__main__":
    main()