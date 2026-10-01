class Estudiante:
    def __init__(self, nombre: str, edad: int, genero: str, calificaciones: list):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.calificaciones = calificaciones

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_informacion(self):
        prom = self.calcular_promedio()
        print(f"Estudiante: {self.nombre} | Edad: {self.edad} | Genero: {self.genero}")
        print(f"Calificaciones: {self.calificaciones} | Promedio: {prom:.2f}\n")


def main():
    estudiantes = [
        Estudiante("Ana Perez", 19, "Femenino", [18.0, 15.5, 17.0, 19.0]),
        Estudiante("Carlos Ramos", 21, "Masculino", [12.0, 14.0, 13.5, 11.0]),
        Estudiante("Maria Gomez", 20, "Femenino", [16.0, 17.0, 18.5, 16.5])
    ]

    print("=== REPORTE DE ESTUDIANTES ===")
    for estudiante in estudiantes:
        estudiante.mostrar_informacion()


if __name__ == "__main__":
    main()