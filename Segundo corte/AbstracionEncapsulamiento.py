from abc import ABC, abstractmethod

#clase Abstracta que define un metodo de pago
class metodoPago(ABC):
    @abstractmethod
    #los metodos que empiecen con una referencia a this
    #o self, son metodos de intacia
    def procesa_pago(this, monto:float):
        pass

#clases concretas: metodos de pago especificos
class TarjetaCredeito(metodoPago):
    def procesa_pago(self, monto: float):
        print(f"Procesando pago de ${monto} con Tarjeta de Crédito")

class PagoMercadoPago(metodoPago):
    def procesa_pago(this, monto):
        #return super().procesa_pago(monto)
        print(f"procesando pago por${monto} de mercado mpago")


#--------ENCAPSULAMIENTO
#INTRO
class Cuentabancaria:
    def __init__(this, titular:str, numero:int, saldoInicial:float):
        #todo los atributos de this y self son de instacioas

        this.titular = titular
        this.numero = numero
        this.saldoInicial = saldoInicial
        
    def obtener_saldo(this):
        return this.saldo
    def hacer_deposito(this, valor:float):
        if valor > 0:
            this.saldo += valor
            print(f"Su deposito es de ${valor} fue exitoso. Nuevo saldo: ${this.saldo}")
        else:
            print("Error: El valor a depositar debe ser mayor a 0.")
            
    def hacer_retiro(this, valor:float):
        if valor > 0:
            if valor <= this.saldo:
                this.saldo -= valor
                print(f"Su retiro de ${valor} fue exitoso. Saldo: ${this.saldo}")
            else:
                print(f"Fondos insuficientes para este retiro.")
        else:
            print(f"Error: El valor a retirar debe ser mayor a 0.")



#----------Herencia
class Empleado(ABC):
    def __init__(this, Nombre:str, id:str, Salario_base:float):
        this.nombre = Nombre
        this.id = id
        this.salario_base = Salario_base

    @abstractmethod
    def liquidarPago(this):
        pass

class Administrativo(Empleado):
    def __init__(this, Nombre:str, id:str, Salario_base:float, bono:float = 0):
        super().__init__(Nombre, id, Salario_base)
        this.bono = (Salario_base * 50) / 100

    def liquidarPago(this):
        pago_total = this.salario_base + this.bono
        print(f"Liquidando Administrativo {this.nombre}: Salario ${this.salario_base} + Bono ${this.bono} = Total ${pago_total}")
        return pago_total

class Docente(Empleado):
    def __init__(this, Nombre:str, id:str, Salario_base:float):
        # Solo llamamos al constructor padre, sin bono
        super().__init__(Nombre, id, Salario_base)

    def liquidarPago(this):
        print(f"Liquidando Docente {this.nombre}: Salario base ${this.salario_base}")
        return this.salario_base