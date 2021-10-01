from threading import Thread, Lock
import threading
mutex = Lock()


def DatosProcesados(data, thread_safe):
    if thread_safe:
        mutex.acquire()
    try:
        thread_id = threading.get_ident()
        print('\nDatos procesados', data, "ThreadId:", thread_id)
    finally:
        if thread_safe:
            mutex.release()


counter = 0
maximo = 100
thread_safe = True
while True:
    some_data = counter
    t = Thread(target=DatosProcesados, args=(some_data, thread_safe))
    t.start()
    counter = counter + 1
    if counter >= maximo:
        break

#Dado el siguiente programa, corregir  sobre el para que los programa para que los subprocesos no se sobrepongan y obtener una salida perfecta, aplicando exlusión mutua

# Ejemplo salida del 0 al 99:
# Processing data: 0 ThreadId: 123145475211264
# Processing data: 1 ThreadId: 123145475211264
# Processing data: 2 ThreadId: 123145475211264
# Processing data: 3 ThreadId: 123145475211264
# Processing data: 4 ThreadId: 123145475211264
# Processing data: 5 ThreadId: 123145475211264