"""
Ejercicio: Programación funcional sobre datos de humedales de Cali.
Completar cada función marcada con # TODO.
No usar bucles for/while explícitos dentro de las funciones (sí se permiten
dentro de comprensiones, ya que no cuentan como bucle explícito).
"""

from functools import reduce


def LoadData(fileName):
    dataset = []
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            dataset.append(registro)
    return dataset


def LoadData_lazy(fileName):
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            yield registro


# ---------------------------------------------------------------------------
# Punto 1

def filtrar_por_estado(dataset, estado):
    estados = estado.strip().lower()
    return filter(
    lambda f: f["estado"].strip().lower() == estados, dataset
    )

# ---------------------------------------------------------------------------
# Punto 2
def extraer_nombres(dataset):
    """Retorna una lista solo con los nombres de los humedales."""
    return list(map(lambda f: f["nombre"], dataset))


# ---------------------------------------------------------------------------
# Punto 3
import functools
def total_hectareas(dataset):
 return functools.reduce(lambda acom, x: acom + x["hectareas"], dataset, 0.0)



# ---------------------------------------------------------------------------
# Punto 4
def promedio_biodiversidad(dataset):
    """Retorna el promedio de (aves + flora) por humedal, usando reduce    (no usar sum() directamente)."""
    suma_total = functools.reduce(lambda acom, x: acom + x["aves"] + x["flora"], dataset, 0)
    return suma_total / len(dataset)


# ---------------------------------------------------------------------------
# Punto 5
def extraer_estados(dataset):
    """Función de apoyo: retorna el conjunto (set) de estados distintos
    presentes en el dataset."""

    return set(map(lambda r: r["estado"], dataset))

def resumen_por_estado(dataset):
    """Retorna un diccionario {estado: cantidad_de_humedales_en_ese_estado},
    construido con una comprensión de diccionarios."""
    # TODO: usar comprensión de diccionarios, apoyándose en extraer_estados
    data = list(dataset)
    return {
        estado: len(list(filter(lambda r: r["estado"] == estado, data)))
        for estado in extraer_estados(data)
    }


# ---------------------------------------------------------------------------
# Punto 6
def humedales_criticos_lazy(fileName, hectareas_min):
    """Retorna un GENERADOR (no una lista) con los humedales cuyo estado es
    'Deteriorado' o cuyas hectáreas son menores a hectareas_min.
    Debe usar LoadData_lazy y filter(), conservando la evaluación perezosa."""
    # TODO: usar LoadData_lazy(fileName) + filter()
    
    return filter(
        lambda f: f["estado"] == "Deteriorado" or f["hectareas"] < hectareas_min,
        LoadData_lazy(fileName)
    )


# ---------------------------------------------------------------------------
# Punto 7 (bonus)
def componer(*funciones):
    """Retorna una nueva función que aplica las funciones recibidas en
    cadena, de derecha a izquierda: componer(f, g)(x) == f(g(x))."""
    return reduce(lambda f, g: lambda x: f(g(x)), funciones)


# ---------------------------------------------------------------------------
if __name__ == "__main__":

    dataset = LoadData("LenguajesProgramacion/humedales.csv")

    print("Humedales en estado Deteriorado:")
    print(filtrar_por_estado(dataset, "Deteriorado"))

    print("\nNombres de todos los humedales:")
    print(extraer_nombres(dataset))

    print("\nTotal de hectáreas:", total_hectareas(dataset))

    print("\nPromedio de biodiversidad (aves+flora):", promedio_biodiversidad(dataset))

    print("\nResumen por estado:")
    print(resumen_por_estado(dataset))

    print("\n\n\nGenerador perezoso (humedales críticos, hectareas_min = 3.0):")
    gen = humedales_criticos_lazy("LenguajesProgramacion/humedales.csv", 3.0)
    print("\n",next(gen))
    print("\n",next(gen))
   

    # Punto 7 (bonus): pipeline con composición de funciones
    # pipeline = componer(sorted, extraer_nombres,
    #                      lambda d: filtrar_por_estado(d, "bueno"))
    # print("\nNombres de humedales en buen estado, ordenados:")
    # print(pipeline(dataset))

