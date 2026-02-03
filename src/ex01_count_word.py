"""
EX01 (Texto) · Buscar una palabra en un fichero

Objetivo:
- Practicar la lectura de ficheros de texto usando `open(...)`.
- Normalizar el contenido (minúsculas) y contar coincidencias.

Consejo:
- No hace falta una solución "perfecta" de NLP.
  Con que cuentes palabras separadas por espacios y elimines puntuación básica es suficiente.
"""

from __future__ import annotations

from pathlib import Path
import string


def count_word_in_file(path: str | Path, word: str) -> int:
    """
    Devuelve el número de apariciones de `word` dentro del fichero de texto `path`.

    Reglas:
    - Búsqueda NO sensible a mayúsculas/minúsculas.
      Ej: "Hola" cuenta como "hola".
    - Cuenta por palabra (no por subcadena).
      Ej: si word="sol", NO debe contar dentro de "solución".
    - Considera puntuación básica como separador (.,;:!? etc.)
      Pista: puedes traducir la puntuación a espacios.

    Errores:
    - Si el fichero no existe, lanza FileNotFoundError.
    - Si word está vacía o solo espacios, lanza ValueError.
    """
    punt=list(string.punctuation) #lista de puntuaciones básicas
    punt.append("etc.") #añadimos "etc." a la lista de puntuaciones
    cont=0
    with open(path , "r", encoding="utf-8") as file:
        if not Path(path).is_file():
            raise FileNotFoundError(f"El fichero {path} no existe.")
        if word.strip()=="":
            raise ValueError('La palabra no puede estar vacía o contener solo espacios.')
        contenido=file.read().lower() #leemos el contenido y lo pasamos a minúsculas
        for p in punt:
            contenido=contenido.replace(p," ") #reemplazamos la puntuación por espacios
            palabras=contenido.split() #separamos el contenido en palabras
        for p in palabras:
            if p==word.lower(): #comparo cada palabra con la palabra buscada
                cont+=1 #incremento el contador si hay coincidencia
    return cont

    raise NotImplementedError("Implementa count_word_in_file(path, word)")
