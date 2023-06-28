from node import Node
"""
Autor: Kevin Andres Acosta Rengifo
fecha: 25/06/2023
Descripción: Clase que representa una lista enlazada
"""


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar(self, data):
        new_node = Node(data)
        current = self.head

        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def eliminar(self, data):
        current = self.head
        before = None
        while current is not None:
            if current.data == data:
                if before is None:
                    self.head = current.next
                else:
                    before.next = current.next
                return True
            before = current
            current = current.next

    def get_index(self, i):
        cnt = 0
        current = self.head
        while cnt < i and current is not None:
            current = current.next
            cnt += 1

        if current is None:
            raise IndexError
        return current.data

    def lenght(self):
        cnt = 0
        current = self.head
        while current is not None:
            current = current.next
            cnt += 1
        return cnt

    def verificar_ordenada(self):
        current = self.head
        num = 0
        if current is None:
            return True
        else:
            while current.next is not None:
                if current.data > current.next.data:
                    num = 1
                    break
                current = current.next
            return num == 0