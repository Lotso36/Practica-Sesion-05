class Empleado:
    def __init__(self, nombre: str, salario: float, cargo: str):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo


class GrupoEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def calcular_salario_promedio(self) -> float:
        if not self.empleados:
            return 0.0
        total_salarios = sum(emp.salario for emp in self.empleados)
        return total_salarios / len(self.empleados)

    def mostrar_resumen(self):
        print("=== LISTA DE EMPLEADOS ===")
        for emp in self.empleados:
            print(f"- {emp.nombre:<20} | {emp.cargo:<15} | S/. {emp.salario:.2f}")
        print(f"\nSalario promedio del grupo: S/. {self.calcular_salario_promedio():.2f}")


def main():
    grupo = GrupoEmpleados()
    grupo.agregar_empleado(Empleado("Lucia Fernandez", 3200.0, "Analista"))
    grupo.agregar_empleado(Empleado("Pedro Huaman", 4500.0, "Desarrollador Senior"))
    grupo.agregar_empleado(Empleado("Raul Morales", 2100.0, "Soporte Tecnico"))
    grupo.agregar_empleado(Empleado("Valeria Castillo", 5800.0, "Jefe de Proyecto"))

    grupo.mostrar_resumen()


if __name__ == "__main__":
    main()