from functools import reduce


def LoadData_lazy(fileName):
    with open(fileName, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = line.split(sep=';')
            if len(values) < 6:
                continue
            yield {
                "nombre":    values[0],
                "direccion": values[1],
                "hectareas": float(values[2]),
                "aves":      int(values[3]),
                "flora":     int(values[4]),
                "estado":    values[5]
            }


def filtrar_por_estado(dataset, estado):
    return filter(
        lambda r: r["estado"].strip().lower() == estado.strip().lower(),
        dataset
    )


def extraer_nombres(dataset):
    return list(map(lambda r: r["nombre"], dataset))


def total_hectareas(dataset):
    return reduce(lambda acc, r: acc + r["hectareas"], dataset, 0)


def promedio_biodiversidad(dataset):
    total, contador = reduce(
        lambda acc, r: (acc[0] + r["aves"] + r["flora"], acc[1] + 1),
        dataset,
        (0, 0)
    )
    return total / contador if contador else 0


CSV_PATH = "LenguajesProgramacion/LAZY--EAGLE/humedales.csv"

print(" Punto 1: Filtrar por estado 'Bueno' ")
print(list(filtrar_por_estado(LoadData_lazy(CSV_PATH), "Bueno")))

print("\n Punto 2: Extraer nombres")
print(extraer_nombres(LoadData_lazy(CSV_PATH)))

print("\n Punto 3: Total de hectáreas")
print(total_hectareas(LoadData_lazy(CSV_PATH)))

print("\n Punto 4: Promedio de biodiversidad ")
print(promedio_biodiversidad(LoadData_lazy(CSV_PATH)))
