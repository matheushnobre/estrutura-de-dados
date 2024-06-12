class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self): # Verifica se a pilha está vazia
         return self.items == []

     def push(self, item): # Insere um novo item à pilha
         self.items.append(item)

     def pop(self): # Remove o primeiro elemento da pilha
         return self.items.pop()

     def peek(self): # Retorna o último elemento da pilha, sem removê-lo
         return self.items[len(self.items)-1]

     def size(self): # Retorna o tamanho da pilha
         return len(self.items)