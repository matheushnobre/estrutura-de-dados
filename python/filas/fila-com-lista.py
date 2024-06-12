class Queue:
    # Inicializa a fila
    def __init__(self):
        self.items = []

    # Retorna se a fila está vazia
    def isEmpty(self):
        return self.items == []

    # Adiciona um elemento na fila
    def enqueue(self, item):
        self.items.insert(0,item)

    # Remove um elemento da fila
    def dequeue(self):
        return self.items.pop()

    # Retorna o tamanho da fila
    def size(self):
        return len(self.items)