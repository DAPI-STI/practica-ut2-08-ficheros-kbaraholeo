"""
EX04 (Texto) · Listín telefónico en fichero

Vas a implementar un pequeño "CRUD" (Crear/Leer/Actualizar/Borrar) de contactos,
guardados en un fichero de texto.

Formato del fichero (una línea por contacto):
nombre,telefono

Ejemplo:
Ana,600123123
Luis,600000000

Para que el ejercicio sea más limpio, se proponen dos funciones "privadas":
- _load_phonebook(): lee el fichero y lo convierte en dict
- _save_phonebook(): guarda el dict en el fichero

Luego, las funciones públicas usan esas helpers:
- add_contact(): alta/actualización
- get_phone(): consulta
- remove_contact(): baja
"""

from __future__ import annotations

from pathlib import Path


def _load_phonebook(path: str | Path) -> dict[str, str]:
    """
    Carga el listín desde `path` y devuelve un diccionario {name: phone}.

    Reglas:
    - Si el fichero no existe, devuelve {} (NO es error).
    - Ignora líneas vacías.
    - Cada línea debe tener exactamente 2 partes separadas por coma:
      "nombre,telefono"
      Si alguna línea está mal formada, lanza ValueError.
    - Recorta espacios alrededor de nombre y teléfono con .strip().

    Consejo:
    - Usa `with open(..., encoding="utf-8") as f:`
    - Recorre línea a línea con `for line in f:`
    """
    with open(path, "r", encoding="utf-8") as file:
        phonebook={} #diccionario vacío para almacenar los contactos
        if not Path(path).is_file():
            return phonebook #si el fichero no existe, devolvemos el diccionario vacío
        for line in file:
            linea=linea.strip() #elimina los espacios en blanco del principio y final de la línea
            if linea=="": #si la línea está vacía, la ignoramos
                continue
            partes=linea.split(",") #separamos la línea en partes usando la coma como separador
            if len(partes)!=2: #si la línea no tiene exactamente 2 partes, lanzamos ValueError
                raise ValueError("Línea mal formada en el fichero.")
            name=partes[0]
            phone=partes[1]
            phonebook[name]=phone #añadimos el contacto al diccionario
        return phonebook #devolvemos el diccionario con los contactos
    raise NotImplementedError("Implementa _load_phonebook(path)")

def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    """
    Guarda el diccionario en `path` en formato "nombre,telefono", una línea por contacto.

    Reglas:
    - Sobrescribe el fichero (modo 'w').
    - Puedes guardar en cualquier orden.
    - Usa encoding="utf-8".
    """
    with open(path, "w", encoding="utf-8")as file:
        for name, phone in phonebook.items(): #Reccorremos el diccionario con items para obtener el nombre y el teléfono de cada contacto
            file.write(f"{name},{phone}\n") #Escribimos cada contacto en el fichero con el formato "nombre, teléfono"
    raise NotImplementedError("Implementa _save_phonebook(path, phonebook)")


def add_contact(path: str | Path, name: str, phone: str) -> None:
    """
    Añade o actualiza un contacto (name -> phone) en el fichero.

    Reglas:
    - name y phone no pueden estar vacíos (tras strip). Si lo están, ValueError.
    - Si el contacto ya existe, se actualiza su teléfono.
    - Si no existe, se añade.

    Pista:
    - load -> modificar dict -> save
    """
    with open(path,"w", encoding="utf-8")as file:
        if name.strip()=="" or phone.strip()=="": #comprbamos si el nombre o el teléfono están vacíos tras elminar los espacios en blanco
            raise ValueError("El nombre y el teléfono no pueden estar vacíos.")
        if not Path(path).is_file(): #si el fichero no existe, creamos un nuevo diccionario con el contacto y lo guardamos
            phonebook={name: phone} #diccionario con el nuevo contacto actualizado
            file.write(f"{name},{phone}\n") #escribimos el nuevo contacto en el fichero
        else: #si el fichero existe, cargamos el diccionario, actualizamos o añadimos el contacto y lo guardamos
            phonebook=_load_phonebook(path) #cargamos el diccionario con los contactos existentes
            phonebook[name]=phone #actualizamos o añadimos el contacto al diccionario
            _save_phonebook(path, phonebook) #guardamos el diccionario actualizado en el fichero
    raise NotImplementedError("Implementa add_contact(path, name, phone)")


def get_phone(path: str | Path, name: str) -> str | None:
    """
    Devuelve el teléfono del contacto `name` o None si no existe.

    Reglas:
    - Si el fichero no existe, devuelve None (porque no hay contactos).
    - `name` se compara tras strip().
    """
    with open(path, "w", encoding="utf-8") as file:
        if not Path(path).is_file(): #si el fichero no existe, devolvemos None
            return None
        if name.strip()=="": #si el nombre está vacío tras eliminar los espacios en blanco, devolvemos None
            return None
        phonebook=_load_phonebook(path) #cargamos el diccionario con los contactos existentes
        if name in phonebook: #si el nombre del contacto existe en el diccionario, devolvemos su teléfono
            return phonebook[name]
    raise NotImplementedError("Implementa get_phone(path, name)")


def remove_contact(path: str | Path, name: str) -> bool:
    """
    Elimina el contacto `name` si existe.

    Devuelve:
    - True si se eliminó
    - False si no existía

    Reglas:
    - Si el fichero no existe, devuelve False.
    - `name` se compara tras strip().

    Pista:
    - load -> borrar si existe -> save si cambió
    """
    with open(path,"w", encoding="utf-8")as file:
        if not Path(path).is_file(): #si el fichero no existe, devolvemos false
            return False
        if name== "": #si el nombre está vacío, devolvemos false
            return False
        phonebook=_load_phonebook(path) #cargamos el diccionario con los contactos existentes
        if name in phonebook: #si el nombre del contacto existe en el diccionario, lo eliminamos y guardamos el diccionario actualizado
            del phonebook[name] #eliminamos el contacto del diccionario
            _save_phonebook(path, phonebook) #guardamos el diccionario actualizado en el fichero
            return True #devolvemos true porque se eliminó el contacto
        else:
            return False #devolvemos false porque no existía el contacto
    
    raise NotImplementedError("Implementa remove_contact(path, name)")
