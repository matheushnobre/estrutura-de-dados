from typing import Any
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self, element):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self._size = self._size + 1
        
    def __len__(self):
        return self._size
    
    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def get(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")
    
    def set(self, index, element):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = element
        else:
            raise IndexError("List index out of range")
        
    def index(self, element):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{element} is not in list")
    
    def insert(self, index, element):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
        
    def remove(self, element):
        if self.head == None:
            raise ValueError(f"{element} not in list")
        elif self.head.data == element:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == element:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{element} not in list")

    def __str__(self):
        pointer = self.head
        string = ''
        if not pointer:
            return 'Empty list'
        while(pointer):
            if pointer.next:
                string += str(pointer.data)+' -> '
            else:
                string += str(pointer.data)
            pointer = pointer.next
        return string

lista = LinkedList()
print("Lista:", lista)
lista.append(2)
lista.append(32)
print("Tamanho:", len(lista))
print("Lista na posição 0:", lista.get(0))
lista.set(0, 25)
print("Elemento na posição 0 modificado")
print("Lista na posição 0:", lista.get(0))
print("Indíce do elemento 32:", lista.index(32))
lista.insert(1, 12)
print("Elemento 12 inserido na posição 1")
print("Lista:", lista)
print("Tamanho:", len(lista))
lista.remove(12)
print("12 removido da lista.")
print("Tamanho:", len(lista))
print("Lista:", lista)
lista.insert(0, 5)
lista.append(88)
print("Lista:", lista)
print("Tamanho:", len(lista))