class Empleado:
    def __init__(self, nombre: str, salario: float, cargo: str):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario: S/. {self.salario:.2f}"


def cargar_empleados(archivo_ruta: str) -> list:
    empleados = []
    try:
        with open(archivo_ruta, "r", encoding="utf-8") as f:
            for nro_linea, linea in enumerate(f, 1):
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nombre = partes[0].strip()
                    try:
                        salario = float(partes[1].strip())
                        cargo = partes[2].strip()
                        empleados.append(Empleado(nombre, salario, cargo))
                    except ValueError:
                        print(f"Aviso: Salario no valido en la linea {nro_linea}. Se omite.")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_ruta}' no fue encontrado.")
    return empleados


if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de empleados (ej. empleados.txt): ").strip()
    lista_empleados = cargar_empleados(nombre_archivo)

    print(f"\nTotal de empleados cargados: {len(lista_empleados)}")
    for emp in lista_empleados:
        print(emp)