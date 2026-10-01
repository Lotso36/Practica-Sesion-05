def convertir_a_mayusculas(archivo_in: str = "entrada.txt", archivo_out: str = "salida.txt"):
    try:
        with open(archivo_in, "r", encoding="utf-8") as f_in:
            contenido = f_in.read()

        contenido_mayus = contenido.upper()

        with open(archivo_out, "w", encoding="utf-8") as f_out:
            f_out.write(contenido_mayus)

        print(f"El texto ha sido convertido a mayusculas y guardado en '{archivo_out}'.")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_in}'.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")


if __name__ == "__main__":
    convertir_a_mayusculas()