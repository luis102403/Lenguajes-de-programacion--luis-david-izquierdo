# 1. DEFINICIÓN DE FUNCIONES (Siempre arriba)
def agregar(lista, elemento):
    lista.append(elemento)
    return lista
 
def eliminar(lista, elemento):
    lista.remove(elemento)
    return lista   

def buscar(lista, elemento):
    return elemento in lista

# 2. VARIABLES Y CÓDIGO PRINCIPAL
Coor_1 =(8,5)
Students=("Ricardo","luis" ,"maria")
Students_list=["Ricardito", "gabriela"]
print(f"\nPrimer matriculado:{Students[0]}")
print(f"\nSegundo matriculado:{Students[1]}")
 
print("Hola, Mundo")

current_year = 2026
tallest_person_height = 2.3
name = input("Cuál es tu nombre?:\n")
b_year = int(input("Cuál es tu año de nacimiento?:\n"))
height = float(input("Cuál es tu estatura?:\n"))
 
age = current_year - b_year
height_difference = (tallest_person_height - height)*100
 
print(f" Te llamas {name} y tienes {age} años. Bienvenido a lenguajes de programación")
print(f"La persona más alta, te lleva {height_difference:.1f} cm.") # Redondeado a 1 decimal
 
empty_list = []
empty_list.append(1)
empty_list.append("Uno")
empty_list.append(1.0)
empty_list.append(True)
 
not_empty_list = empty_list
# reversed_list = not_empty_list.reverse() # Ojo: .reverse() modifica la lista original y devuelve None.

students = ("Ricardo Stiven","Gabriela","Andrea") 
students_list = ["Ricardo Stiven","Gabriela","Andrea"]

print( f"\nPrimero se matriculó: {students[0]}")
print(f"\nLuego se matriculó: {students[1]}")
print(f"\nFinalmente se matriculó: {students[2]}")
 
students_list[1] = "Gabriela Rico"
# AHORA SÍ FUNCIONA PORQUE LA FUNCIÓN YA EXISTE
students_list = agregar(students_list, "Diego")
 
print("\nLista actual de estudiantes:")
print(students_list)
 
# 3. MENÚ CONDICIONAL
while True:
    opcion = int(input("\nQué operación desea aplicar? 1. Agregar 2. Eliminar 3. Buscar 4. Salir: "))
    
    if opcion == 1:
        funcion = agregar 
    elif opcion == 2:
        funcion = eliminar
    elif opcion == 3:
        funcion = buscar
    else:
        break
 
    valor = input("Ingrese el valor: ")
    
    # Manejo de la función buscar vs agregar/eliminar
    if opcion == 3:
        resultado = funcion(students_list, valor)
        print(f"¿El elemento '{valor}' está en la lista?: {resultado}")
    else:
        students_list = funcion(students_list, valor)
        print(f"Lista actualizada: {students_list}")