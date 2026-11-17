#funcion para un consumidor hambriento
def eager():
    numbers=[]
    for i in range(1000000):
        numbers.append(i)
        return numbers


#funcion peresoza genera valores bajo demanda
def lazy_generator():
    for i in range(100000):
        yield i

#consumo con evaluacion hambrienta
#nuevos_numeros = eager()
#print(nuevos_numeros)

#consumo con evaluacion perezosa

#yield: genera un valor---- suspende la ejecucion y espera un next del consumidor
gen = lazy_generator()

try: 
    while True:
      #el consumidor perezoso consume solo un elemento a la vez:
      print(next(gen))
except StopIteration:
    print("El generado ya no tiene mas numeros")

#para leer un texto plano
# archivo = open("", "r", encoding="utf-8")

# try:
#     while True:
#         # Lee línea por línea perezosamente
#         linea = next(archivo)
#         print(linea.strip())
# except StopIteration:
#     print("Llegamos al final del archivo de texto.")
# finally:
#     archivo.close()

#para aun CSV
# import csv

# archivo_csv = open("datos.csv", "r", encoding="utf-8")
# lector = csv.reader(archivo_csv)

# try:
#     while True:
#         # Extrae la siguiente fila como una lista
#         fila = next(lector)
#         print(fila)
# except StopIteration:
#     print("Fin del archivo CSV.")
# finally:
#     archivo_csv.close()


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

#Función para crear un "dataset" como una lista de diccionarios
#a partir de un archivo plano
#param: la ruta del archivo plano
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

eager_eval = LoadData("humedales_cali.csv")
print("todos los registro \n", eager_eval)

lazy_eval= LoadData_lazy("humedales_cali.csv")
print(next(lazy_eval))