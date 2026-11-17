def LoadData(fileName):
    dataset = []
    with open(fileName,encoding='utf-8') as f:
        for line in f: #iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            dataset.append(registro)    
    return dataset
from functools import reduce
eager_eval = LoadData("LenguajesProgramacion/LAZY--EAGLE/humedales.csv")
# print("todos los registro \n", eager_eval)

# --- Punto 1 ---
def filtrar_por_estado(dataset, estado):
    return filter( lambda x: x["estado"].strip().lower() == estado.strip().lower(),dataset
    )

# --- Punto 2 ---
def extraer_nombres(dataset):
    return list(map(lambda r: r["nombre"], dataset))

# --- Punto 3 ---
def total_hectareas(dataset):
    return functools.reduce(lambda acom, r: acom + r["hectareas"], dataset, 0)
import functools
# # Punto 3
# def total_hectareas(dataset):
#     return functools.reduce(lambda acumulador, x: acumulador + x["hectareas"], dataset, 0.0)
# --- Punto 4 ---
def promedio_biodiversidad(dataset):
    total, contador = reduce(
        lambda acom, r: (acom[0] + r["aves"] + r["flora"], acom[1] + 1),
        dataset,
        (0, 0)
    )
    return total / contador if contador else 0

eager_eval = LoadData("LenguajesProgramacion/LAZY--EAGLE/humedales.csv")

# print(list(filtrar_por_estado(eager_eval, "Bueno")))
# print(extraer_nombres(eager_eval))
# print(total_hectareas(eager_eval))
# print(promedio_biodiversidad(eager_eval))

