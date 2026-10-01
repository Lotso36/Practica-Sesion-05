import string
from collections import Counter

def extraer_palabras_unicas(archivo_origen: str, archivo_destino: str = "palabras_unicas.txt"):
    try:
        with open(archivo_origen, "r", encoding="utf-8") as fin:
            texto = fin.read()

        tabla_traduccion = str.maketrans("", "", string.punctuation)
        texto_limpio = texto.translate(tabla_traduccion).lower()
        palabras = texto_limpio.split()

        conteo = Counter(palabras)
        palabras_unicas = [palabra for palabra, cant in conteo.items() if cant == 1]
        palabras_unicas.sort()

        with open(archivo_destino, "w", encoding="utf-8") as fout:
            for palabra in palabras_unicas:
                fout.write(f"{palabra}\n")

        print(f"Se encontraron {len(palabras_unicas)} palabras que aparecen una sola vez.")
        print(f"Exportadas correctamente a '{archivo_destino}'.")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_origen}'.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo a analizar: ").strip()
    extraer_palabras_unicas(archivo)