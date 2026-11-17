import threading
import time


def timer(id_temp,duration):
    for i in range (1, duration+1):
        print (f"hilo{id_temp}, tick{i}")
        time.sleep(0.5)
    print(f"hilo {id_temp} termino")

#creamos 2 hilos con distinta duracion

hilo1= threading.Thread(target=timer, args=(1,5))
hilo2= threading.Thread(target=timer, args=(2,2))
print(f"hilo main ... lamando hilos secundarios")
hilo1.start()
hilo2.start()

print(f"hilos main ejecutandose ")
hilo1.join()

print(f"hilo main... el hilo 1 ya termino, vamos a esperar el hilo 2....")

hilo2.join()

print(f" terminaron los dos ")