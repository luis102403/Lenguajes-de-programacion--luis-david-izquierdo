# PRINCIPIOS SOLID APLICADOS A LA PROGRAMACION ORIENTADA A OBJETOS
# S - Single Responsibility Principle
# O - Open/Closed Principle
# L - Liskov Substitution Principle
# I - Interface Segregation Principle
# D - Dependency Inversion Principle

from abc import ABC, abstractmethod


# ============================================================
# S - SINGLE RESPONSIBILITY PRINCIPLE

class Matricula:
    def __init__(self, valor):
        self.valor = valor


class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo


# O - OPEN / CLOSED PRINCIPLE

class Descuento(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


# Matricula sin descuento
class MatriculaSinDescuento(Descuento):

    def calcular(self, valor):
        return 0


# Descuento por matrícula de honor
class DescuentoMatriculaHonor(Descuento):

    def calcular(self, valor):
        return valor * 0.50


# Descuento por monitorías
class DescuentoMonitorias(Descuento):

    def calcular(self, valor):
        return valor * 0.20


# Descuento por convenio
class DescuentoPorConvenio(Descuento):

    def calcular(self, valor):
        return valor * 0.10


# ============================================================
# L - LISKOV SUBSTITUTION PRINCIPLE
# Cualquier implementación de Descuento puede usarse de forma
# intercambiable sin alterar el comportamiento esperado.
# ============================================================

descuentos = [
    DescuentoMatriculaHonor(),
    DescuentoMonitorias(),
    DescuentoPorConvenio()
]

# Se puede iterar por la lista y aplicar cada descuento sin problema,
# porque todas las subclases cumplen el contrato de Descuento.


class Descuento(ABC):
    @abstractmethod
    def calcular(self, valor_base):
        pass


class validacionElegibilidad(ABC):
    @abstractmethod
    def validar(self, estudiante):
        pass


# ============================================================
# D - DEPENDENCY INVERSION PRINCIPLE
#
# El módulo de alto nivel (LiquidacionMatricula) NO depende de
# clases concretas (DescuentoMatriculaHonor, DescuentoMonitorias...).
# Depende de la ABSTRACCIÓN (Descuento).
#
# Flujo:
#           LiquidacionMatricula
#                   |
#             Descuento (ABC)        <-- abstracción
#                   |
#       ┌───────────┼───────────┐
#       |           |           |
# MatriculaHonor  Monitorias  Convenio
class LiquidacionMatricula:

    # DIP: recibe la abstracción Descuento, no una clase concreta
    def __init__(self, descuento: Descuento):
        self.descuento = descuento

    def liquidar(self, valor_base: float):
        valor_descuento = self.descuento.calcular(valor_base)
        total_pagar = valor_base - valor_descuento
        return total_pagar, valor_descuento


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código del estudiante: ")

    valor = float(input("Ingrese el valor de la matrícula: $"))

    matricula = Matricula(valor)
    estudiante = Estudiante(nombre, codigo)

    # Seleccionar el tipo de descuento
    print("\nTipos de descuento disponibles:")
    print("1. Matrícula de honor (50%)")
    print("2. Monitorías (20%)")
    print("3. Convenio (10%)")
    print("4. Sin descuento (0%)")

    opcion = input("Seleccione el descuento (1-4): ")

    if opcion == "1":
        descuento = DescuentoMatriculaHonor()
    elif opcion == "2":
        descuento = DescuentoMonitorias()
    elif opcion == "3":
        descuento = DescuentoPorConvenio()
    elif opcion == "4":
        descuento = MatriculaSinDescuento()
    else:
        print("Opción no válida.")
        exit()

    # DIP en acción: se inyecta la dependencia concreta desde afuera
    liquidacion = LiquidacionMatricula(descuento)

    total, valor_descuento = liquidacion.liquidar(matricula.valor)

    # Mostrar los resultados
    print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")
    print(f"Nombre: {estudiante.nombre}")
    print(f"Código: {estudiante.codigo}")

    print("\n--- RESUMEN DE MATRÍCULA ---")
    print(f"Valor de la matrícula: ${matricula.valor:,.0f}")
    print(f"Valor del descuento:   ${valor_descuento:,.0f}")
    print(f"Total a pagar:         ${total:,.0f}")
