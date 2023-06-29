"""
Autores: Kevin Acosta
         Ronan Moreno
         Rodolfo Bolaños
fecha: 27/06/2023
Descripción: Clase nodo , clase obra y la clase de lista enlazada para las obras del museo
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.ptrNext = None


class Obra:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


class LinkedListObra:
    def __init__(self):
        self.head = None

    def insert(self, obra):
        node = Node(obra)

        current = self.head

        if current is None:
            self.head = node
        else:
            while current.ptrNext is not None:
                current = current.ptrNext

            current.ptrNext = node

    def getIndex(self, i):
        cnt = 0
        current = self.head
        while cnt < i and current is not None:
            current = current.ptrNext
            cnt += 1

        if current is None:
            # raise OverflowError
            print("no hay existencia de la obra ")

        return current.value

    def delete(self, obra):
        current = self.head
        before = None
        while current is not None and current.value != obra:
            before = current
            current = current.ptrNext

        if current is None:
            raise ReferenceError

        if before is None:
            self.head = current.ptrNext
        else:
            before.ptrNext = current.ptrNext

    def listarReplicas(self):
        current = self.head
        while current is not None:
            print(
                f"Obra: {current.value.nombre}, Cantidad: {current.value.cantidad}")
            current = current.ptrNext
