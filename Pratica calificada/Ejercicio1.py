def filtrar_multiplos():
    nombre_archivo = input("Ingrese el nombre del archivo a evaluar (ej. entrada_propuesto1.txt): ").strip()
    
    try:
        n = int(input("Ingrese el numero n del cual desea obtener los multiplos: "))
        if n == 0:
            print("Error: El numero n no puede ser cero.")
            return

        with open(nombre_archivo, "r", encoding="utf-8") as archivo_in:
            lineas = archivo_in.read().split()

        multiplos = []
        for valor in lineas:
            try:
                num = int(valor)
                if num % n == 0:
                    multiplos.append(num)
            except ValueError:
                continue

        archivo_salida = "multiplos.txt"
        with open(archivo_salida, "w", encoding="utf-8") as archivo_out:
            for num in multiplos:
                archivo_out.write(f"{num}\n")

        print(f"\nProceso completado con exito.")
        print(f"Se encontraron {len(multiplos)} multiplos de {n}. Guardados en '{archivo_salida}':")
        for num in multiplos:
            print(f" - {num}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except ValueError:
        print("Error: Por favor, ingrese un numero entero valido para n.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")


if __name__ == "__main__":
    filtrar_multiplos()