from fila import Queue

def batataQuente(listaNomes, num):
    fila = Queue()
    for nome in listaNomes:
        fila.enqueue(nome)
    
    while fila.size() > 1:
        for i in range(num):
            fila.enqueue(fila.dequeue())
        fila.dequeue()
        
    return fila.dequeue()

print(batataQuente(["Bill","David","Susan","Jane","Kent","Brad"],7))
