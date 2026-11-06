from abc import ABC, abstractmethod
# Dependency Inversion Principle: Un modulo de alto nivel no debe depender de módulos de bajo nivel, ambos deben depender de abstracciones. Las abstracciones no deben depender de los detalles, los detalles deben depender de las abstracciones.


# Sistema de notificaciones:
# NO APLICA BIEN EL PRINCIPIO DIP

class EmailSender:
    def sendEmail(self, message):
        print(f"Enviando notificación{message}")


class notificationService:
    def __init__(self):
        #Ya estoy amarrando la funcionalidad a una implementacion concreta
        self.sender = EmailSender

    def sendNotification(self, message):
        self.sender.sendEmail(message)


#COMO LO SOLUCIONAMOS:

#Creamos una interfaz que define el contrato de las notificaciones
class INotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender:
    def sendEmail(self, message):
        print(f"Enviando notificación{message}")

class SMSSender(INotificationService):
    def send(self, message):
        print(f"enviando notificacion:{message}, por email")

class whatsappSender(INotificationService):
    def send(self, message):
        print(f"enviando notificacion:{message}, por email")


class NotificationService:
    def __init__(self, sender:INotificationService):
        self.sender = sender

    def sendNotification(self, message):
        self.sender.send(message)

sender_via_SMS = SMSSender()
MyNotificationService = INotificationService(sender_via_SMS)
MyNotificationService.send("hola, ya llego el pedido")