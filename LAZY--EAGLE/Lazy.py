def LoadData_lazy(fileName):
    dataset = []
    with open(fileName,encoding='utf-8') as f:
        for line in f: 
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            yield registro

lazy_eval = LoadData_lazy("LenguajesProgramacion/LAZY--EAGLE/humedales.csv")
# print(next(lazy_eval))


from functools import reduce


# --- Punto 1 ---
def filtrar_por_estado(dataset, estado):
    return filter(
        lambda f: f["estado"].strip().lower() == estado.strip().lower(),
        dataset
    )

# --- Punto 2 ---
def extraer_nombres(dataset):
    return list(map(lambda f: f["nombre"], dataset))

# --- Punto 3 ---
def total_hectareas(dataset):
    return reduce(lambda acc, f: acc + f["hectareas"], dataset, 0)

# --- Punto 4 ---
def promedio_biodiversidad(dataset):
    total, contador = reduce(
        lambda acc, f: (acc[0] + f["aves"] + f["flora"], acc[1] + 1),
        dataset,
        (0, 0)
    )
    return total / contador if contador else 0

Lazy = LoadData_lazy("LenguajesProgramacion/LAZY--EAGLE/humedales.csv")

# print(list(filtrar_por_estado(Lazy, "Bueno")))
# print(extraer_nombres(Lazy))
# print(total_hectareas(Lazy))
# print(promedio_biodiversidad(Lazy))

# --- Demostración lazy de map ---
hum_nombres = map(lambda r: r["nombre"], LoadData_lazy("LenguajesProgramacion/LAZY--EAGLE/humedales.csv"))

print("nombre con next():")
print(next(hum_nombres))  

# print("\nCon for:")
# for h in hum_nombres:   
#     print(h)