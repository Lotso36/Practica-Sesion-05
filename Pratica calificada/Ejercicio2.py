def reemplazar_en_archivo():
    archivo_origen = input("Ingrese el nombre del archivo origen: ").strip()
    texto_buscar = input("Ingrese el texto a buscar: ")
    texto_reemplazo = input("Ingrese el texto a reemplazar: ")
    archivo_destino = input("Ingrese el nombre del archivo de salida: ").strip()

    if not texto_buscar:
        print("Error: El texto a buscar no puede estar vacio.")
        return

    total_reemplazos = 0

    try:
        with open(archivo_origen, "r", encoding="utf-8") as fin, \
             open(archivo_destino, "w", encoding="utf-8") as fout:
            
            for linea in fin:
                conteo_linea = linea.count(texto_buscar)
                total_reemplazos += conteo_linea
                linea_modificada = linea.replace(texto_buscar, texto_reemplazo)
                fout.write(linea_modificada)

        print(f"\nArchivo generado: '{archivo_destino}'")
        print(f"Total de reemplazos realizados: {total_reemplazos}")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_origen}'.")
    except Exception as e:
        print(f"Ocurrio un error durante el procesamiento: {e}")


if __name__ == "__main__":
    reemplazar_en_archivo()