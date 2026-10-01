
import os

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_stock: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def to_csv_line(self) -> str:
        return f"{self.nombre},{self.precio},{self.cantidad_stock}\n"

    def __str__(self):
        return f"Nombre: {self.nombre:<18} | Precio: S/. {self.precio:<8.2f} | Stock: {self.cantidad_stock}"


class Tienda:
    ARCHIVO_DATOS = "productos.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):
        if not os.path.exists(self.ARCHIVO_DATOS):
            return

        try:
            with open(self.ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) == 3:
                        nombre = partes[0].strip()
                        precio = float(partes[1].strip())
                        stock = int(partes[2].strip())
                        self.productos[nombre.lower()] = Producto(nombre, precio, stock)
        except Exception as e:
            print(f"Error al cargar datos desde '{self.ARCHIVO_DATOS}': {e}")

    def guardar_productos(self):
        try:
            with open(self.ARCHIVO_DATOS, "w", encoding="utf-8") as f:
                for prod in self.productos.values():
                    f.write(prod.to_csv_line())
            print(f"Datos guardados exitosamente en '{self.ARCHIVO_DATOS}'.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_producto(self):
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
            return

        clave = nombre.lower()
        if clave in self.productos:
            print(f"El producto '{nombre}' ya existe. Use la opcion de actualizar si desea modificarlo.")
            return

        try:
            precio = float(input("Precio: "))
            stock = int(input("Cantidad en stock: "))
            if precio < 0 or stock < 0:
                print("El precio y el stock deben ser valores positivos.")
                return

            self.productos[clave] = Producto(nombre, precio, stock)
            print(f"Producto '{nombre}' agregado correctamente.")
        except ValueError:
            print("Entrada invalida. Ingrese valores numericos para precio y stock.")

    def mostrar_productos(self):
        print("\n--- LISTA DE PRODUCTOS ---")
        if not self.productos:
            print("No hay productos registrados.")
            return

        for prod in self.productos.values():
            print(prod)

    def buscar_producto(self):
        print("\n--- BUSCAR PRODUCTO ---")
        nombre = input("Ingrese el nombre del producto: ").strip()
        prod = self.productos.get(nombre.lower())
        if prod:
            print("\nProducto encontrado:")
            print(prod)
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

    def actualizar_precio(self):
        print("\n--- ACTUALIZAR PRECIO ---")
        nombre = input("Ingrese el nombre del producto: ").strip()
        prod = self.productos.get(nombre.lower())
        if not prod:
            print(f"El producto '{nombre}' no existe.")
            return

        try:
            nuevo_precio = float(input(f"Precio actual: S/. {prod.precio:.2f}. Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.")
                return
            prod.precio = nuevo_precio
            print(f"Precio de '{prod.nombre}' actualizado a S/. {nuevo_precio:.2f}.")
        except ValueError:
            print("Error: Ingrese un valor numerico valido.")

    def eliminar_producto(self):
        print("\n--- ELIMINAR PRODUCTO ---")
        nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
        clave = nombre.lower()
        if clave in self.productos:
            del self.productos[clave]
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print(f"El producto '{nombre}' no existe.")

    def menu(self):
        while True:
            print("\n==============================")
            print("     GESTION DE PRODUCTOS     ")
            print("==============================")
            print("1. Agregar producto")
            print("2. Mostrar lista de productos")
            print("3. Buscar producto por nombre")
            print("4. Actualizar precio de un producto")
            print("5. Eliminar producto")
            print("6. Salir")
            opcion = input("Seleccione una opcion (1-6): ").strip()

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_precio()
            elif opcion == "5":
                self.eliminar_producto()
            elif opcion == "6":
                self.guardar_productos()
                print("Programa finalizado.")
                break
            else:
                print("Opcion no valida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    app = Tienda()
    app.menu()