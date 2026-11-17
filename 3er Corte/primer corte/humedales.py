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

def LoadData_lazy(fileName):
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
            yield registro


eager_eval = LoadData("LenguajesProgramacion/humedales.csv")
print("todos los registro \n", eager_eval)

lazy_eval = LoadData_lazy("LenguajesProgramacion/humedales.csv")
print(next(lazy_eval))


# # Punto 1
# def filtrar_por_estado(dataset, estado):
#     """Retorna los registros cuyo 'estado' coincide con el parámetro dado
#     (comparación insensible a mayúsculas/minúsculas y espacios)."""
#     estado_buscado = estado.strip().lower()
#     return list(filter(lambda f: f["estado"].strip().lower() == estado_buscado, dataset))


 # Punto 2
def extraer_nombres(dataset):
     """Retorna una lista solo con los nombres de los humedales."""
     return list(map(lambda f: f["nombre"], dataset))

import functools
# # Punto 3
# def total_hectareas(dataset):
#     """Retorna la suma total de hectáreas de todos los humedales."""
#     return functools.reduce(lambda acumulador, x: acumulador + x["hectareas"], dataset, 0.0)


# # Punto 4
# def promedio_biodiversidad(dataset):
#     """Retorna el promedio de (aves + flora)"""
#     if not dataset:
#         return 0.0
    
#     suma_total = functools.reduce(lambda acc, x: acc + x["aves"] + x["flora"], dataset, 0)
#     return suma_total / len(dataset)