import threading
import time

# Vehículos esperando turno (cola de espera)
vehiculos = [
    ("Tesla",    3),
    ("BYD",      4),
    ("Kia",      3),
    ("Deepal",   4),
    ("Mercedes", 2),
    ("Renault",  5),
    ("Xiaomi",   1),
]

def isla_de_carga(id_isla):
    # Aquí la isla tomará vehículos de la cola (sincronización pendiente)
    print(f"[Isla {id_isla}] Lista para recibir vehículos.")

# 5 hilos = 5 islas de carga
hilo_isla1 = threading.Thread(target=isla_de_carga, args=(1,))
hilo_isla2 = threading.Thread(target=isla_de_carga, args=(2,))
hilo_isla3 = threading.Thread(target=isla_de_carga, args=(3,))
hilo_isla4 = threading.Thread(target=isla_de_carga, args=(4,))
hilo_isla5 = threading.Thread(target=isla_de_carga, args=(5,))

hilo_isla1.start()
hilo_isla2.start()
hilo_isla3.start()
hilo_isla4.start()
hilo_isla5.start()

hilo_isla1.join()
hilo_isla2.join()
hilo_isla3.join()
hilo_isla4.join()
hilo_isla5.join()

print("Todos los vehículos han sido atendidos. Estación cerrada.")
