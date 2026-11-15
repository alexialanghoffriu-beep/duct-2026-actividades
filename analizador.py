import string

STOP_WORDS = {
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una",
    "que", "es", "por", "con", "no", "se", "su", "al", "lo", "como",
}


def tokenizar(texto):
    """
        Convierte el texto a minusculas, quita los signos de puntuacion
        y lo separa en una lista de palabras (tokens).
    
        Parametros:
            texto (str): texto crudo a procesar
    
    Retorna:
            list[str]: lista de tokens limpios
        """
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return texto.split()


def contar_frecuencias_texto(texto):
    """Recibe un STRING. Es la que usan los tests."""
    frecuencias = {}
    for palabra in tokenizar(texto):
        if palabra not in STOP_WORDS:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def contar_frecuencias(ruta):
    """
    Lee un archivo de texto y devuelve un diccionario con la
    frecuencia de cada palabra.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return contar_frecuencias_texto(archivo.read())


def analizar_y_graficar(ruta, top_n=10):
    """
        Lee un archivo de texto, cuenta la frecuencia de cada palabra
        y genera un grafico de barras horizontales con las top_n
        palabras mas frecuentes.
    
        Parametros:
            ruta (str): ruta al archivo de texto a analizar
            top_n (int): cantidad de palabras a graficar
    
        Retorna:
            None (genera y guarda el grafico)
        """ 
    import matplotlib.pyplot as plt  
    frecuencias = contar_frecuencias(ruta)
    top = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [par[0] for par in top]
    valores = [par[1] for par in top]

    plt.figure(figsize=(10, 6))
    plt.bar(palabras, valores, color="pink")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


def main():
    frecuencias = contar_frecuencias("texto_integradora.txt")

    print(f"Cantidad de palabras totales: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")
    print("\nLas 10 palabras mas frecuentes:")

    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")

    analizar_y_graficar("texto_integradora.txt")


if __name__ == "__main__":
    main()