import threading
import time

def task_1(dest, msg, seconds):
   print(f"Ejecutando {msg} para {dest}")
   #simular retraso:
   time.sleep(seconds)


#crear hilos
hilo1 = threading.Thread(target=task_1, args=("diego", "hola", 10))
hilo2 = threading.Thread(target=task_1, args=("diana", "chao", 8))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

#las siguientes lineas de codigo se ejecutan cuando todos los hilos terminan ..

print("todos los hilos")