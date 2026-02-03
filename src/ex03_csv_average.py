"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""
from __future__ import annotations
import csv

from pathlib import Path




def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.

    Reglas:
    - El CSV tiene cabecera.
    - `column` debe existir en la cabecera. Si no, ValueError.
    - Todos los valores de esa columna deben poder convertirse a float. Si no, ValueError.
    - Si no hay filas de datos (CSV vacío tras la cabecera), ValueError.
    - Si el fichero no existe, FileNotFoundError.

    Ejemplo:
    name,average
    Ana,10
    Luis,6

    csv_average(..., "average") -> 8.0
    """
    with open(path, "r", encoding="utf-8") as file:
        if not Path(path).is_file():
            raise ValueError("El fichero no existe.")
        datos=csv.DictReader(file) #dictreader para leer el csv como diccionario. Es decir nos da cabeceras y valores(columnas)
        op1=0.0 #operando1 para la suma de las notas
        contador=0 #contador para contar el número de notas
        for fila in datos:
            if column not in fila:
                raise ValueError("La columna no existe en la cabecera.")
            else:
                op1+=float(fila[column]) #sumamos la nota convertida a float
                contador+=1 #incrementamos el contador
        if contador==0:
            raise ValueError("No hay filas de datos en el CSV.")
        media=op1/contador
        return media #devolvemos la media
    
    raise NotImplementedError("Implementa csv_average(path, column)")
